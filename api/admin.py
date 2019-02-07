from django.contrib import admin
from .models import Airline, Airport, Route

# Register your models here.

admin.site.register(Airline)
admin.site.register(Airport)
admin.site.register(Route)
