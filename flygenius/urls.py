from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from api import views

class WelcomeView(routers.APIRootView):
    """
    
    These data are being used to predict flight times and compare airlines at FlyGenius. 
    [Check it out](https://flygeni.us) if you haven't already!
    # About the API
    
    The FlyGenius API contains statistics from all U.S. Domestic flights during the three year
    period 2015-18. The original dataset comes from the Bureau of Transportation Statistics and can be 
    [found here](https://www.transtats.bts.gov/DatabaseInfo.asp?DB_ID=120&DB_Name=Airline%20On-Time%20Performance%20Data)
    in its original csv form. 

    Each flight in the dataset has been pulled out and used to create statistics for the relevant airports, airline, and route. 
    We've computed averages and rankings for a variety of useful metrics from the original dataset. 

    ## Data classes 
    There are three main models in the FlyGenius API:  

     - [Airlines](https://api.flygeni.us/airlines)
     - [Airports](https://api.flygeni.us/airports)
     - [Routes](https://api.flygeni.us/routes)
    
    """
    pass


class DocumentedRouter(routers.DefaultRouter):
    APIRootView = WelcomeView


router = DocumentedRouter()
router.register(r'airlines', views.AirlineViewSet)
router.register(r'airports', views.AirportViewSet)
router.register(r'routes', views.RouteViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),

]