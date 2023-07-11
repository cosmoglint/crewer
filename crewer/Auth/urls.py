from .views import UserViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls')),
]