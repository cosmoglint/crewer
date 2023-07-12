from django.core.exceptions import ValidationError
from django.db import models
from .constants import TASK_STATES, PROFICIENCY_NOT_WITHIN_RANGE
from .helper import *



class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    project = models.ForeignKey("ProjectManager.Project", on_delete=models.CASCADE)
    assignee = models.ForeignKey("Auth.User", on_delete=models.SET_NULL, blank=True, null=True )
    status = models.IntegerField(default=0, choices=TASK_STATES)
    effort_estimate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

class Skill(models.Model):
    name = models.CharField(max_length=150)
    proficiency = models.FloatField(default=0.0)
    description = models.TextField(null=True)

    def save(self, *args, **kwargs):
        if validate_within_min(self.proficiency) and validate_within_max(self.proficiency):
            super().save(*args, **kwargs)
        else:
            raise ValidationError(PROFICIENCY_NOT_WITHIN_RANGE)
