from django.db import models
from .constants import TASK_STATES


class Task(models.Model):
    name = models.CharField(max_length=150)
    project = models.ForeignKey("ProjectManager.Project", on_delete=models.CASCADE)
    assignee = models.ForeignKey("User", on_delete=models.SET_NULL, blank=True, null=True )
    status = models.IntegerField(default=0, choices=TASK_STATES)
    description = models.TextField()
    effort_estimate = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # skills to-do: skills
