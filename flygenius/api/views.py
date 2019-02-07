from .models import Airline, Airport, Route
from rest_framework import viewsets
from  .serializers import AirlineSerializer, AirportSerializer, RouteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class AirlineViewSet(viewsets.ModelViewSet):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('airline_name', 
                    'airline_id', 
                    'airline_ontime_departure_rank',
                    'airline_ontime_arrival_rank',
                    'airline_arrival_delay',
                    'airline_departure_delay',
                    'airline_flights_per_day')


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('airport_name',
                    'airport_id',
                    'airport_city',
                    'airport_state',
                    'airport_ontime_departure_rank',
                    'airport_ontime_arrival_rank',
                    'airport_arrival_delay',
                    'airport_departure_delay',
                    'airport_flights_per_day')


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('route_name',
                    'route_time',
                    'route_origin_airport',
                    'route_destination_airport',
                    'route_airlines',
                    'route_flight_volume',
                    'route_flights_per_day')