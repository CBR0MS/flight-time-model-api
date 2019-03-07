from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from apiManagement.models import Email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.utils.html import strip_tags

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        to_email = instance.email

        email_content_obj = Email.objects.get(name='registered_new_user')
        from_email = email_content_obj.email_name + ' <' + email_content_obj.send_from + '>'
        content = {'user': instance.username, 'token': token}

        open('flygenius/templates/temp_email.html', 'w').close()
        text_file = open('flygenius/templates/temp_email.html', 'w')
        text_file.write(email_content_obj.content)
        text_file.close()

        html_template = get_template('temp_email.html')
        html_content = html_template.render(content)
        plain_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(email_content_obj.subject, plain_content, from_email, [to_email] )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()


class Airport(models.Model):
    airport_name = models.CharField(max_length=60)
    airport_id = models.CharField(max_length=3)
    airport_city = models.CharField(max_length=60)
    airport_state = models.CharField(max_length=2)
    airport_percent_ontime_departure = models.PositiveSmallIntegerField(null=True)
    airport_taxi_in_time = models.SmallIntegerField(null=True)
    airport_taxi_out_time = models.SmallIntegerField(null=True)
    airport_departures_per_year = models.PositiveIntegerField(null=True)
    airport_arrivals_per_year = models.PositiveIntegerField(null=True)
    airport_departure_delay = models.SmallIntegerField(null=True)
    airport_destinations = models.ManyToManyField('api.Airport', blank=True)
    airport_airlines = models.ManyToManyField('api.Airline', blank=True)
    airport_flight_volume_rank = models.PositiveSmallIntegerField(null=True)
    airport_ontime_departure_rank = models.PositiveSmallIntegerField(null=True)
    url = models.URLField(null=True)
    database_id = models.AutoField(primary_key=True)
    
    def save(self, *args, **kwargs):
        new_url = 'https://api.flygeni.us/airports/' + str(self.database_id) + '/'
        self.url = new_url 
        super(Airport, self).save(*args, **kwargs)


    def __str__(self):
        return self.airport_name + ' (' + self.airport_id + ')'

class Airline(models.Model):
    airline_name = models.CharField(max_length=30)
    airline_id = models.CharField(max_length=3)
    airline_percent_ontime_arrival = models.PositiveSmallIntegerField(null=True)
    airline_flights_per_year = models.PositiveIntegerField(null=True)
    airline_departure_delay = models.SmallIntegerField(null=True)
    airline_arrival_delay = models.SmallIntegerField(null=True)
    airline_destinations = models.ManyToManyField('api.Airport', blank=True)
    airline_ontime_departure_rank = models.PositiveSmallIntegerField(null=True)
    airline_ontime_arrival_rank = models.PositiveSmallIntegerField(null=True)
    airline_flight_volume_rank = models.PositiveSmallIntegerField(null=True)
    url = models.URLField(null=True)
    database_id = models.AutoField(primary_key=True)
    
    def save(self, *args, **kwargs):
        new_url = 'https://api.flygeni.us/airlines/' + str(self.database_id) + '/'
        self.url = new_url 
        super(Airline, self).save(*args, **kwargs)

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
    url = models.URLField(null=True)
    database_id = models.AutoField(primary_key=True)

    def save(self, *args, **kwargs):
        new_url = 'https://api.flygeni.us/routes/' + str(self.database_id) + '/'
        self.url = new_url 
        super(Route, self).save(*args, **kwargs)

    def __str__(self):
        return self.route_name