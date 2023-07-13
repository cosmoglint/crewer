
from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProjectList.as_view()),
    path("tasks/<int:pk>", views.ProjectTaskList.as_view()),
    path("allocate/<int:project>/", views.ProjectAllocate.as_view()),
    path("<int:pk>/", views.ProjectDetail.as_view())
]