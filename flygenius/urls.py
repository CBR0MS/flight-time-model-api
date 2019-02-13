from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from api import views
from rest_framework.authtoken import views as authviews

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

    ## Access to the API

    GET requests to the API are limited to 20 per day for unregistered users. Registered users can make up to 400 requests per day.
    To register, [visit the sign up page](https://api.flygeni.us/signup). Upon registration, you'll receive an email containing your 
    token. Keep this token secure and be sure not to include it in any files that you publicly commit. 

    ## Authentication
    To make a request to the API as a registered user, you'll need either your token or username and password. 

    ### Authentication with a token 
    To authenticate with your token, include the following in any request you make to the API:

        Authorization: Token <your-token>
    For example, making a request with curl would look like this:

        curl -X GET https://api.flygeni.us/airlines -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
    
    Or, using python with the [requests](http://docs.python-requests.org/en/master/) package:
    
        import requests
        response = requests.get('https://api.flygeni.us/airlines', headers={'Authorization': 'Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'})

    ### Authentication with your user credentials
    It is best to avoid this method if possible, as it requires another step on top of token authentication.
    To authenticate with your username and password, you must first request a token. Do this by making a POST request to 
    `api-token-auth/` with your username and password, like this:

        https://api.flygeni.us/api-token-auth/ username='<your-username>' password='<your-password>'
    
    You should get a json object as a response with your token:

        {
            "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
        }
    Now, you can authenticate with this token as described in the previous section. 


    ## Root List
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
    path('api-token-auth/', authviews.obtain_auth_token, name='api-token-auth'),
    path('signup', views.signup, name='signup')

]