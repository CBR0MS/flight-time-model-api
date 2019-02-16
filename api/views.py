from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from rest_framework.response import Response
from rest_framework.request import clone_request
from rest_framework import status, viewsets, filters

from api.forms import SignUpForm
from api.responses import add_auth_to_response

from .models import Airline, Airport, Route
from .serializers import AirlineSerializer, AirportSerializer, RouteSerializer



class StandardHTTPResponses(viewsets.ModelViewSet):

    def list(self, request):
        serializer = self._serializer(self.queryset, many=True)
        return add_auth_to_response(Response(serializer.data), request)

    def retrieve(self, request, pk=None):
        airline = get_object_or_404(self.queryset, pk=pk)
        serializer = self._serializer(airline)
        return add_auth_to_response(Response(serializer.data), request)

    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))
        serializer = self._serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return add_auth_to_response(Response(serializer.data), request)

    def update(self, request, *args, **kwargs):
        instance = self.get_object_or_none()
        serializer = self._serializer(instance, data=request.data)
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

class AirlineViewSet(StandardHTTPResponses):

    http_method_names = ['get', 'options', 'head', 'patch', 'put']
    queryset = Airline.objects.all()
    _serializer = AirlineSerializer



class AirportViewSet(StandardHTTPResponses):

    http_method_names = ['get', 'options', 'head', 'patch', 'put']
    queryset = Airport.objects.all()
    _serializer = AirportSerializer


class RouteViewSet(StandardHTTPResponses):

    http_method_names = ['get', 'options', 'head', 'patch', 'put']
    queryset = Route.objects.all()
    _serializer = RouteSerializer
 
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



