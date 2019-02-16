from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from rest_framework.authtoken import views as authviews

from api import views


class WelcomeView(routers.APIRootView):
    pass


class DocumentedRouter(routers.DefaultRouter):
    APIRootView = WelcomeView


router = DocumentedRouter()
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