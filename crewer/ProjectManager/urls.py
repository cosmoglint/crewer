
from django.urls import path

from . import views

urlpatterns = [
    path("oldlist", views.project_list, name="projectlist"),
    path("allocate/<int:project>/", views.allocate_tasks, name="allocate"),
    path("", views.ProjectList.as_view()),
    path("<int:pk>/", views.ProjectDetail.as_view())
]