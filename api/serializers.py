from .models import Airline, Airport, Route
from rest_framework import serializers

# serializers with hyperlinks for ManyToMany fields 

class AirlineSerializerHyperlinks(serializers.ModelSerializer):
    airline_destinations = serializers.SlugRelatedField(
        many=True,
        queryset=Airport.objects.all(),
        slug_field='url'
    )
    class Meta:
        model = Airline
        fields = '__all__'

class AirportSerializerHyperlinks(serializers.ModelSerializer):
    airport_destinations = serializers.SlugRelatedField(
        many=True,
        queryset=Airport.objects.all(),
        slug_field='url'
    )
    airport_airlines = serializers.SlugRelatedField(
        many=True,
        queryset=Airline.objects.all(),
        slug_field='url'
    )
    class Meta:
        model = Airport
        fields = '__all__'

class RouteSerializerHyperlinks(serializers.ModelSerializer):
    route_airlines = serializers.SlugRelatedField(
        many=True,
        queryset=Airline.objects.all(),
        slug_field='url'
    )
    route_origin_airport = serializers.SlugRelatedField(
        many=False,
        queryset=Airport.objects.all(),
        slug_field='url'
    )
    route_destination_airport = serializers.SlugRelatedField(
        many=False,
        queryset=Airport.objects.all(),
        slug_field='url'
    )
    class Meta:
        model = Route 
        fields = '__all__'

# list hyperlink serializers 
class AirlineSerializerListHyperlinks(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ('url',)
class AirportSerializerListHyperlinks(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ('url',)
class RouteSerializerListHyperlinks(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('url',)

# serializers with airline/airport ids for ManyToMany fields 

class AirlineSerializerIds(serializers.ModelSerializer):
    airline_destinations = serializers.SlugRelatedField(
        many=True,
        queryset=Airport.objects.all(),
        slug_field='airport_id'
    )
    class Meta:
        model = Airline
        fields = '__all__'

class AirportSerializerIds(serializers.ModelSerializer):
    airport_destinations = serializers.SlugRelatedField(
        many=True,
        queryset=Airport.objects.all(),
        slug_field='airport_id'
    )
    airport_airlines = serializers.SlugRelatedField(
        many=True,
        queryset=Airline.objects.all(),
        slug_field='airline_id'
    )
    class Meta:
        model = Airport
        fields = '__all__'

class RouteSerializerIds(serializers.ModelSerializer):
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

# list id serializers 
class AirlineSerializerListIds(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ('airline_id',)
class AirportSerializerListIds(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ('airport_id',)
class RouteSerializerListIds(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('route_name',)

# serializers with primary keys for ManyToMany fields 
class AirlineSerializerPks(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'
class AirportSerializerPks(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'
class RouteSerializerPks(serializers.ModelSerializer):
    class Meta:
        model = Route 
        fields = '__all__'

# list pk serializers 
class AirlineSerializerListPks(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ('database_id',)
class AirportSerializerListPks(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ('database_id',)
class RouteSerializerListPks(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('database_id',)


