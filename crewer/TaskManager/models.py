import datetime

from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models
from .constants import *
from .helper import *


class Skill(models.Model):
    name = models.CharField(max_length=150)
    proficiency = models.FloatField(default=0.0)
    description = models.TextField(null=True)

    def __unicode__(self):
        return u'%s' % (self.name)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if validate_within_min(self.proficiency) and validate_within_max(self.proficiency):
            super().save(*args, **kwargs)
        else:
            raise ValidationError(PROFICIENCY_NOT_WITHIN_RANGE)

class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    project = models.ForeignKey("ProjectManager.Project", on_delete=models.CASCADE)
    assignee = models.ForeignKey("Auth.User", on_delete=models.SET_NULL, blank=True, null=True )
    skills = models.ManyToManyField("Skill", blank=True, null=True)
    status = models.IntegerField(default=0, choices=settings.TASK_STATES)
    effort_estimate = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    class Meta:
        ordering = ["start_date"]

    def __unicode__(self):
        return u'%s' % (self.name)

    def __str__(self):
        return self.name

    def unassign(self):
        success, reason = False, "Error"
        if self.status == settings.COMPLETED:
            reason = "already completed"
        else:
            self.assignee = None
            self.status = settings.UNASSIGNED
            self.save()
            success = True
            reason = "successfully unassigned"

    def assign(self, user):
        success = False
        available, reason = user.is_available(self)
        print("availability within assign", available, reason)
        if available:
            try:
                self.assignee = user
                self.status = settings.ASSIGNED
                user.tasks.add(self)
                user.save()
                self.save()
                success = True
                reason = "successfully assigned"
            except Exception as e:
                success = False
                reason = str(e)
                print("failed to assign and save task:", reason)
                # to-do: log stuff
        return success, reason

    def save( self, *args, **kwargs):

        if not(self.end_date):
            self.end_date = diff_time_calculator(self.start_date, self.effort_estimate)

        super().save(*args, **kwargs)
