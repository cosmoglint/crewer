from .views import UserViewSet
from rest_framework import routers, urls
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    # path('login', CustomAuthToken.as_view(), name='login'),
    # path('logout', LogoutView.as_view(), name='logout'),
    path('', include('rest_framework.urls')),
]