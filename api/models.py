from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Airport(models.Model):
    airport_name = models.CharField(max_length=30)
    airport_id = models.CharField(max_length=3)
    airport_city = models.CharField(max_length=30)
    airport_state = models.CharField(max_length=2)
    airport_percent_ontime_departure = models.PositiveSmallIntegerField(null=True)
    airport_taxi_in_time = models.SmallIntegerField(null=True)
    airport_taxi_out_time = models.SmallIntegerField(null=True)
    airport_departures_per_year = models.PositiveIntegerField(null=True)
    airport_arrivals_per_year = models.PositiveIntegerField(null=True)
    airport_departure_delay = models.SmallIntegerField(null=True)
    airport_destinations = models.ManyToManyField('api.Airport')
    airport_airlines = models.ManyToManyField('api.Airline')
    airport_flight_volume_rank = models.PositiveSmallIntegerField(null=True)
    airport_ontime_departure_rank = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.airport_name + ' (' + self.airport_id + ')'

class Airline(models.Model):
    airline_name = models.CharField(max_length=30)
    airline_id = models.CharField(max_length=3)
    airline_percent_ontime_arrival = models.PositiveSmallIntegerField(null=True)
    airline_flights_per_year = models.PositiveIntegerField(null=True)
    airline_departure_delay = models.SmallIntegerField(null=True)
    airline_arrival_delay = models.SmallIntegerField(null=True)
    airline_destinations = models.ManyToManyField('api.Airport')
    airline_ontime_departure_rank = models.PositiveSmallIntegerField(null=True)
    airline_ontime_arrival_rank = models.PositiveSmallIntegerField(null=True)
    airline_flight_volume_rank = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.airline_name + ' (' + self.airline_id + ')'

class Route(models.Model):
    route_name = models.CharField(max_length=30)
    route_time = models.PositiveSmallIntegerField(null=True)
    route_origin_airport = models.ForeignKey('api.Airport', on_delete=models.CASCADE, related_name='origin_airport')
    route_destination_airport = models.ForeignKey('api.Airport', on_delete=models.CASCADE, related_name='destination_airport')
    route_airlines = models.ManyToManyField('api.Airline')
    route_flights_per_year = models.PositiveIntegerField(null=True)
    route_flight_volume_rank = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.route_name