from .models import Airline, Airport, Route
from rest_framework import serializers

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):

    route_airlines = serializers.SlugRelatedField(
        many=True,
        queryset=Airline.objects.all(),
        slug_field='airline_id'
    )

    route_origin_airport = serializers.SlugRelatedField(
        many=False,
        queryset=Airport.objects.all(),
        slug_field='airport_id'
    )

    route_destination_airport = serializers.SlugRelatedField(
        many=False,
        queryset=Airport.objects.all(),
        slug_field='airport_id'
    )

    class Meta:
        model = Route 
        fields = '__all__'
