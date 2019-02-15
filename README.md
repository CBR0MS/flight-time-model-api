# FlyGenius API Documentation

## About the API

This is the API behind the flight time prediction and airline comparison done at FlyGenius. [Check out the website](https://flygeni.us) if you haven't already!

The FlyGenius API contains a compilation of statistics from all U.S. Domestic flights during the three year period 2015-18. The original dataset comes from the Bureau of Transportation Statistics and can be [found here](https://www.transtats.bts.gov/DatabaseInfo.asp?DB_ID=120&DB_Name=Airline%20On-Time%20Performance%20Data) in its original `.csv` form.
    
Each flight in the dataset has been pulled out and used to create statistics for the relevant airports, airline, and route. We've computed averages and rankings for a variety of useful metrics from the original dataset. This API is useful for gaining insight into overall trends in airline and airport performance, rather than information about specific flights. If you're interested in individual flights, let us know, as this is a feature we're thinking about implementing if there's enough demand. 

## Accessing the API

The FlyGenius API is available for use free of charge. We strongly encourage users to [create an account](https://api.flygeni.us/api-auth/signup/) and get an API token for access, as doing so will grant you 1,000 requests per day. If you do not make an account and make a request without a token, you will be limited to just 20 requests per day. So please, make an account!

If you require more than 1,000 requests, please contact us.


### Making Requests
    
After signing up and getting your token via email, you are ready to make a request to the API. In the examples below, we're going to be using [httpie](https://httpie.org/), though curl or an equivalent program will work fine. A simple, unauthenticated request looks like this:
```Shell
$ http https://api.flygeni.us/airlines/
```

### Making Authenticated Requests with a Token

To make a request with your authentication token, you need to include the following in your request header:
```
Authorization: Token <your-token>
```
Making a request with a token would look like this:
```Shell
$ http http://api.flygeni.us/airlines/ "Authorization: Token daa1c80567404b25f3f36f1a37fd670d6dceeb29"
```
Or, using python with the [requests](http://docs.python-requests.org/en/master/) package:
```python
import requests
response = requests.get('https://api.flygeni.us/airlines', headers={'Authorization': 'Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'})
```
Notice that whenever you make a GET request while authenticated, you should see your token and username in the returned header:
```HTTP
HTTP/1.1 200 OK
Auth: 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
User: <your-username>
{ ... }
```
If you are not authenticated, you'll see the following:
```HTTP
HTTP/1.1 200 OK
Auth: None
User: AnonymousUser
{ ... }
```

### Authentication without a Token
If you don't have your token, you can always request it using your username and password. To do this, make a POST request to `api-token-auth/` with your username and password, like this:
```Shell
$ http https://api.flygeni.us/api-token-auth/ username="<your-username>" password="<your-password>"
```
You should get a json object as a response with your token:
```HTTP
HTTP/1.1 200 OK
Content-Type: application/json
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```
Now, you can authenticate with this token as described in the [previous section](#making-authenticated-requests-with-a-token). 

## Resources in the API
There are three main resources in the API; [Airlines](#welcome-to-the-flygenius-api-resources-in-the-api-airlines), [Airports](#welcome-to-the-flygenius-api-resources-in-the-api-airports), and [Routes](#welcome-to-the-flygenius-api-resources-in-the-api-routes).
### Root 
`/` - A list of all resources

A request might look like this:
```HTTP
$ http https://api.flygeni.us/
```
The response:
```HTTP
HTTP/1.1 200 OK
Content-Type: application/json
{
    "airlines": "http://api.flygeni.us/airlines/",
    "airports": "http://api.flygeni.us/airports/",
    "routes": "http://api.flygeni.us/routes/"
}
```

###  Airlines

`/airlines/` - A list of all airlines. 

`/airlines/<id>/` - The specific airline requested 

 A request might look like this:
```HTTP
$ http https://api.flygeni.us/airlines/1/
```
The response:
```HTTP
HTTP/1.1 200 OK
Content-Type: application/json
{

}
```
#### Attributes 
Each airline has the following attributes:


Attribute | Type | Description 
------|-----|-----
`airline_name` | *String* | The name of the airline.
`airline_id` | *String* | The unique 2 character ID for each airline. 
`airline_percent_ontime_arrival` | *Positive Integer* | Percent of flights that arrive ontime or early. 
`airline_flights_per_year` | *Positive Integer* | The average number of flights per year of the airline. 
`airline_departure_delay` | *Integer* | The average departure time, in minutes, of the airline, relative to scheduled departure. Negative numbers indicate early departures, positive numbers indicate late departures. 
`airline_arrival_delay` | *Integer* | The same as `airline_departure_delay`, except for arrivals. 
`airline_destinations` | *String List* | Airports that the airline flies to. 
`airline_ontime_departure_rank` | *Positive Integer* | The airline's ranking for ontime departures relative to all other airlines. An airline with a rank of 1 indicates it has the most ontime departures compared to all other airlines. 
`airline_ontime_arrival_rank` | *Positive Integer* | The same as `airline_ontime_departure_rank`, but for arrivals.
`airline_flight_volume_rank` | *Positive Integer* | The number of flights flown by the airline per year, relative to all other airlines. 1 indicates most flights, 2 second most, and so on. 

### Airports 

`/airports/` - A list of all airports. 

`/airports/<id>/` - The specific airport requested 

 A request might look like this:
```HTTP
$ http https://api.flygeni.us/airports/12/
```
The response:
```HTTP
HTTP/1.1 200 OK
Content-Type: application/json
{

}
```
#### Attributes 
Each airport has the following attributes:


Attribute | Type | Description 
------|-----|-----
`airport_name` | *String* | The name of the airport. 
`airport_id` | *String* | The unique 3 character ID for each airport. 
`airport_city` | *String* | The city of the airport. 
`airport_state` | *String* | The 2 character state code of the airport. 
`airport_percent_ontime_departure` | *Positive Integer* | Percent of flights that depart ontime or early.
`airport_taxi_in_time` | *Positive Integer* | Average taxi in time, in minutes, for flights arriving at the airport. 
`airport_taxi_out_time` | *Positive Integer* | Average taxi out time, in minutes, for flights departing the airport. 
`airport_departures_per_year` | *Positive Integer* | The average number of departures per year of the airport.
`airport_arrivals_per_year` | *Positive Integer* | The average number of arrivals per year of the airport. 
`airport_departure_delay` | *Integer* | The average departure time, in minutes, of flights at the airport, relative to scheduled departure. Negative numbers indicate early departures, positive numbers indicate late departures. 
`airport_destinations` | *String List* | Airports that the can be flown to from the airport nonstop. 
`airport_airlines` | *String List* | Airlines that fly to the airport.  
`airport_flight_volume_rank` | *Positive Integer* | The number of flights flown to and from the airport per year, relative to all other airports. 1 indicates most flights, 2 second most, and so on. 
`airline_ontime_departure_rank` | *Positive Integer* | The airport's ranking for ontime departures relative to all other airports. An airport with a rank of 1 indicates it has the most ontime departures compared to all other airports. 

### Routes 

`/routes/` - A list of all routes. 

`/routes/<id>/` - The specific route requested 

Note that routes are uni-directional, or **one way**. The route from San Francsico to Seattle includes information for just the one direction; there is a separate route for Seattle to San Francisco. 

A request might look like this:
```HTTP
$ http https://api.flygeni.us/routes/2/
```
The response:
```HTTP
HTTP/1.1 200 OK
Content-Type: application/json
{

}
```

#### Attributes 
Each route has the following attributes:

Attribute | Type | Description 
------|-----|-----
`route_name` | *String* | The name of the route. Constructed by concatenating the ID of the origin airport with the ID of the destination, with an underscore between, like 'SFO_SEA'.
`route_time` | *Positive Integer* | The average flight duration from origin to destination, in minutes.  
`route_origin_airport` | *String* | The origin airport of the route. 
`route_destination_airport` | *String* | The destination airport of the route. 
`route_airlines` | *String List* | The airlines that fly the route nonstop. 
`route_flights_per_year` | *Positive Integer* | Average number of flights per year flown on the route. 
`route_flight_volume_rank` | *Positive Integer* | The route's ranking for number of flights flown per year, relative to all other routes. A route with rank 1 would be most flown, 2 second most, and so on. 
    


