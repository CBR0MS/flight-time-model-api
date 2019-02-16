from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from rest_framework.authtoken import views as authviews
from rest_framework.views import APIView
from rest_framework.response import Response

from api import views
from api.responses import add_auth_to_response



class RootView(APIView):

    def get(self, request, format=None):
       
        content = {
            'airlines': 'https://api.flygeni.us/airlines/',
            'airports': 'https://api.flygeni.us/airports/',
            'routes': 'https://api.flygeni.us/routes/'
        }
        return add_auth_to_response(Response(content), request)

    def get_api_root_dict(self, request):
        api_root_dict = OrderedDict()
        api_root_dict['airlines'] = 'https://api.flygeni.us/airlines/'
        api_root_dict['airports'] = 'https://api.flygeni.us/airports/'
        api_root_dict['routes'] = 'https://api.flygeni.us/routes/'
        return api_root_dict

class Router(routers.DefaultRouter):
    include_root_view = True
    #APIRootView = RootView
    def get_api_root_view(self, api_urls=None):
        return RootView.as_view()

router = Router()
router.register(r'airlines', views.AirlineViewSet, basename='airlines')
router.register(r'airports', views.AirportViewSet, basename='airports')
router.register(r'routes', views.RouteViewSet, basename='routes')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api-token-auth/', authviews.obtain_auth_token, name='api-token-auth'),
    path('api-auth/signup/', views.signup, name='signup'),
    path('docs/', views.docs, name='docs'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)