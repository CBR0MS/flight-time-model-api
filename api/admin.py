from django.contrib import admin
from .models import Airline, Airport, Route
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ('user',)

admin.site.register(Airline)
admin.site.register(Airport)
admin.site.register(Route)
