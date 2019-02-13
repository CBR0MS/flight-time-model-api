from .models import Airline, Airport, Route
from rest_framework import viewsets
from  .serializers import AirlineSerializer, AirportSerializer, RouteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class AirlineViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all airlines. 

    ## Fields 
    Each airline has the following fields:

    `airline_name`
    The name of the airline, as a string.

    `airline_id`
    The unique 2 character ID for each airline. 
    
    `airline_percent_ontime_arrival`
    Percent of flights that arrive ontime or early.
    
    `airline_flights_per_year`
    The average number of flights per year of the airline. 

    `airline_departure_delay`
    The average departure time, in minutes, of the airline, relative to scheduled departure. 
    Negative numbers indicate early departures, positive numbers indicate late departures. 

    `airline_arrival_delay`
    The same as departure delay, except for arrivals. 
    
    `airline_destinations`
    Airports that the airline flies to. 

    `airline_ontime_departure_rank`
    The airline's ranking for ontime departures relative to all other airlines. 
    An airline with a rank of 1 indicates it has the most ontime departures compared
    to all other airlines. 

    `airline_ontime_arrival_rank`
    The same as ontime departure rank, but for arrivals.

    `airline_flight_volume_rank`
    The number of flights flown by the airline per year, relative to all other airlines. 
    1 indicates most flights, 2 second most, and so on. 
    
    ## Searching
    
    Make a seach with 

        GET /airlines/?search=query
    where the query might be an ID like 'UA', or a name like 'United Airlines' 
    or any of the fields listed above. 

    ## Airlines
    """
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('airline_name',
                    'airline_id',
                    'airline_percent_ontime_arrival',
                    'airline_flights_per_year',
                    'airline_departure_delay',
                    'airline_arrival_delay',
                    'airline_destinations',
                    'airline_ontime_departure_rank',
                    'airline_ontime_arrival_rank',
                    'airline_flight_volume_rank')


class AirportViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all airports. 

    ## Fields 
    Each airport has the following fields:

    `airport_name`
    The name of the airport, as a string.

    `airport_id`
    The unique 3 character ID for each airport. 

    `airport_city`
    The city of the airport, as a string. 

    `airport_state`
    The 2 character state code of the airport.
    
    `airport_percent_ontime_departure`
    Percent of flights that arrive ontime or early.
    
    `airport_taxi_in_time`
    Average taxi in time, in minutes, for flights arriving at the airport. 

    `airport_taxi_out_time`
    Average taxi out time, in minutes, for flights departing the airport.

    `airport_departures_per_year`
    The average number of departures per year of the airport. 
    
    `airport_arrivals_per_year`
    The average number of arrivals per year of the airport. 

    `airport_departure_delay`
    The average departure time, in minutes, of flights at the airport, relative to scheduled departure. 
    Negative numbers indicate early departures, positive numbers indicate late departures. 

    `airport_destinations`
    Airports that the can be flown to from the airport nonstop.

    `airport_airlines`
    Airlines that fly to the airport.  

    `airport_flight_volume_rank`
    The number of flights flown to and from the airport per year, relative to all other airports. 
    1 indicates most flights, 2 second most, and so on. 

    `airline_ontime_departure_rank`
    The airport's ranking for ontime departures relative to all other airports. 
    An airport with a rank of 1 indicates it has the most ontime departures compared
    to all other airports. 
    
    ## Searching
    
    Make a seach with 

        GET /airports/?search=query
    where the query might be an ID like 'SFO', or a name like 'San Francisco International' 
    or any of the fields listed above. 

    ## Airports
    """
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('airport_name',
                    'airport_id',
                    'airport_city',
                    'airport_state',
                    'airport_percent_ontime_departure',
                    'airport_taxi_in_time',
                    'airport_taxi_out_time',
                    'airport_departures_per_year',
                    'airport_arrivals_per_year',
                    'airport_departure_delay',
                    'airport_destinations',
                    'airport_airlines',
                    'airport_flight_volume_rank',
                    'airport_ontime_departure_rank')


class RouteViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all routes. 

    Note that routes are directional and *one way*. 
    The route from San Francsico to Seattle includes information for just the one direction; 
    there would be a separate route for Seattle to San Francisco. 

    ## Fields 
    Each route has the following fields:

    `route_name`
    The name of the route, as a string. Constructed by concatenating the ID of the
    origin airport with the ID of the destination, with an underscore between, like 'SFO_SEA'.

    `route_time`
    The average flight duration from origin to destination, in minutes.  

    `route_origin_airport`
    The origin airport of the route. 

    `route_destination_airport`
    The destination airport of the route. 
    
    `route_airlines`
    The airlines that fly the route nonstop. 
    
    `route_flights_per_year`
    Average number of flights per year flown on the route. 

    `route_flight_volume_rank`
    The route's ranking for number of flights flown per year, relative to all 
    other routes. A route with rank 1 would be most flown, 2 second most, and so on. 
    
    ## Searching
    
    Make a seach with 

        GET /route/?search=query
    where the query might be an name like 'SFO_SEA' or a time like '190' 
    or any of the fields listed above. 

    ## Airports
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('route_name',
                    'route_time',
                    'route_origin_airport',
                    'route_destination_airport',
                    'route_airlines',
                    'route_flights_per_year',
                    'route_flight_volume_rank',)