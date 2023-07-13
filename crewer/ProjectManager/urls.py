
from django.urls import path

from . import views

urlpatterns = [
    path("allocate/<int:project>/", views.allocate_tasks, name="allocate"),
    path("", views.ProjectList.as_view()),
    path("tasks/<int:pk>", views.ProjectTaskList.as_view()),
    path("<int:pk>/", views.ProjectDetail.as_view())
]