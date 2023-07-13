from . import views
from django.urls import path, include



urlpatterns = [
    path('users/', views.UserViewSet.as_view(), name='user'),
    path('users/profile/', views.UserProfileView.as_view(), name='profile'),
    path('users/profile/<int:id>', views.UserDetail.as_view(), name='userdetail'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('', include('rest_framework.urls')),
    # path('logout', LogoutView.as_view(), name='logout'),
]