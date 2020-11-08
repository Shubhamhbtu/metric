from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'metric', views.MyDataViewSet)
router.register(r'metric/<int:minute>', views.MyDataViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    #path("metric/<int:minute>/", views.MyDataViewSet),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]