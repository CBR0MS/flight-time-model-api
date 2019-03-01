from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from rest_framework.response import Response
from rest_framework.request import clone_request
from rest_framework import status, viewsets, filters

from api.forms import SignUpForm
from api.responses import add_auth_to_response

from .models import Airline, Airport, Route
from .serializers import AirlineSerializerHyperlinks, AirportSerializerHyperlinks, RouteSerializerHyperlinks
from .serializers import AirlineSerializerIds, AirportSerializerIds, RouteSerializerIds
from .serializers import AirlineSerializerPks, AirportSerializerPks, RouteSerializerPks
from .serializers import AirportSerializerListHyperlinks, AirlineSerializerListHyperlinks, RouteSerializerListHyperlinks
from .serializers import AirportSerializerListPks, AirlineSerializerListPks, RouteSerializerListPks
from .serializers import AirportSerializerListIds, AirlineSerializerListIds, RouteSerializerListIds
from .serializers import AirportSerializerListDetails, AirlineSerializerListDetails

class StandardHTTPResponses(viewsets.ModelViewSet):
    http_method_names = ['get', 'options', 'head', 'patch', 'put']
    # determine which serializer we should use
    def get_serializer(self, request, list_mode=False):
        this_serializer = self._serializer
        if list_mode:
            this_serializer = self.list_serializer
        ids = request.GET.get('use_rc_ids', '')
        pks = request.GET.get('use_db_ids', '')
        details = request.GET.get('use_details', '')

        if ids.lower() == 'true':
            this_serializer = self.id_serializer
            if list_mode:
                this_serializer = self.list_id_serializer
        elif pks.lower() == 'true':
            this_serializer = self.pk_serializer
            if list_mode:
                this_serializer = self.list_pk_serializer
        elif details.lower() == 'true' and list_mode:
            this_serializer = self.list_details_serializer
        return this_serializer

    def list(self, request):
        this_serializer = self.get_serializer(request, list_mode=True)
        serializer = this_serializer(self.queryset, many=True)
        return add_auth_to_response(Response(serializer.data), request)

    def retrieve(self, request, pk=None):
        airline = {}
        try:
            airline = get_object_or_404(self.queryset, pk=pk)
        except ValueError:
            airline = self.get_object_or_404_with_string(pk)
        
        this_serializer = self.get_serializer(request)
        serializer = this_serializer(airline)
        return add_auth_to_response(Response(serializer.data), request)

    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))
        this_serializer = self.get_serializer(request)
        serializer = this_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return add_auth_to_response(Response(serializer.data), request)

    def update(self, request, *args, **kwargs):
        instance = self.get_object_or_none()
        this_serializer = self.get_serializer(request)
        serializer = this_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        if instance is None:
            lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
            lookup_value = self.kwargs[lookup_url_kwarg]
            extra_kwargs = {self.lookup_field: lookup_value}
            serializer.save(**extra_kwargs)
            return add_auth_to_response(Response(serializer.data, status=status.HTTP_201_CREATED), request)

        serializer.save()
        return add_auth_to_response(Response(serializer.data), request)

    def get_object_or_none(self):
        try:
            return self.get_object()
        except Http404:
            if self.request.method == 'PUT':
                self.check_permissions(clone_request(self.request, 'POST'))
            else:
                raise
    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(self, request, *args, **kwargs)

class AirlineViewSet(StandardHTTPResponses):

    queryset = Airline.objects.all()
    list_serializer = AirlineSerializerListHyperlinks
    list_pk_serializer = AirlineSerializerListPks
    list_id_serializer = AirlineSerializerListIds
    list_details_serializer = AirlineSerializerListDetails
    _serializer = AirlineSerializerHyperlinks
    pk_serializer = AirlineSerializerPks
    id_serializer = AirlineSerializerIds
    http_method_names = ['get', 'options', 'head', 'patch', 'put']

    def get_object_or_404_with_string(self, query):
        return get_object_or_404(self.queryset, airline_id=query)

class AirportViewSet(StandardHTTPResponses):

    queryset = Airport.objects.all()
    list_serializer = AirportSerializerListHyperlinks
    list_pk_serializer = AirportSerializerListPks
    list_id_serializer = AirportSerializerListIds
    list_details_serializer = AirportSerializerListDetails
    _serializer = AirportSerializerHyperlinks
    pk_serializer = AirportSerializerPks
    id_serializer = AirportSerializerIds
    http_method_names = ['get', 'options', 'head', 'patch', 'put']

    def get_object_or_404_with_string(self, query):
        return get_object_or_404(self.queryset, airport_id=query)


class RouteViewSet(StandardHTTPResponses):

    http_method_names = ['get', 'options', 'head', 'patch', 'put']
    queryset = Route.objects.all()
    list_serializer = RouteSerializerListHyperlinks
    list_pk_serializer = RouteSerializerListPks
    list_id_serializer = RouteSerializerListIds
    list_details_serializer = RouteSerializerListIds
    _serializer = RouteSerializerHyperlinks
    pk_serializer = RouteSerializerPks
    id_serializer = RouteSerializerIds

    def get_object_or_404_with_string(self, query):
        return get_object_or_404(self.queryset, route_name=query)
 
    # queryset = Route.objects.all()
    # serializer_class = RouteSerializer
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('route_name',
    #                 'route_time',
    #                 'route_origin_airport',
    #                 'route_destination_airport',
    #                 'route_airlines',
    #                 'route_flights_per_year',
    #                 'route_flight_volume_rank',)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/docs/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def docs(request):
    return render(request, 'documentation.html')



