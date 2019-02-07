from django.db import models

class Airport(models.Model):
    airport_name = models.CharField(max_length=30)
    airport_id = models.CharField(max_length=3)
    airport_city = models.CharField(max_length=30)
    airport_state = models.CharField(max_length=2)
    airport_ontime_departure_rank = models.PositiveSmallIntegerField()
    airport_ontime_arrival_rank = models.PositiveSmallIntegerField()
    airport_arrival_delay = models.SmallIntegerField()
    airport_departure_delay = models.SmallIntegerField()
    airport_flights_per_day = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.airport_name + ' (' + self.airport_id + ')'

class Airline(models.Model):
    airline_name = models.CharField(max_length=30)
    airline_id = models.CharField(max_length=3)
    airline_ontime_departure_rank = models.PositiveSmallIntegerField()
    airline_ontime_arrival_rank = models.PositiveSmallIntegerField()
    airline_arrival_delay = models.SmallIntegerField()
    airline_departure_delay = models.SmallIntegerField()
    airline_flights_per_day = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.airline_name + ' (' + self.airline_id + ')'

class Route(models.Model):
    route_name = models.CharField(max_length=30)
    route_time = models.PositiveSmallIntegerField()
    route_origin_airport = models.ForeignKey('api.Airport', on_delete=models.CASCADE, related_name='origin_airport')
    route_destination_airport = models.ForeignKey('api.Airport', on_delete=models.CASCADE, related_name='destination_airport')
    route_airlines = models.ManyToManyField('api.Airline')
    route_flights_per_day = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.route_name