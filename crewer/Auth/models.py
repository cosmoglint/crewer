from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from TaskManager.models import Task
from .constants import RESOURCE_FREE, RESOURCE_UNAVAILABLE

class User(AbstractUser):
    '''
    Custom user model with skill and assigned task data
    '''
    skills = models.ManyToManyField("TaskManager.Skill", blank=True)
    role = models.PositiveSmallIntegerField(choices=settings.ROLE_CHOICES, default=settings.MEMBER)
    tasks = models.ManyToManyField("TaskManager.Task", blank=True)

    def is_member(self):
        return self.role==settings.MEMBER

    def is_manager(self):
        return self.role==settings.MANAGER

    def is_available(self, new_task):
        new_task_start_date, new_task_end_date = new_task.start_date, new_task.end_date
        assigned_tasks = Task.objects.filter(assignee=self).order_by('start_date')
        print("assigned_tasks", assigned_tasks)
        available = False
        reason = RESOURCE_UNAVAILABLE
        task_count = len(assigned_tasks)
        if task_count == 0:
            available = True
            reason = RESOURCE_FREE
        else:
            for i in range(task_count):
                assigned_task = assigned_tasks[i]
                if assigned_task.start_date < new_task_start_date:
                    if assigned_task.end_date < new_task_start_date:
                        if i == task_count-1:
                            available = True
                            reason = RESOURCE_FREE
                            break
                        subsequent_task = assigned_tasks[i + 1]
                        if subsequent_task.start_date > new_task_end_date:
                            available = True
                            reason = RESOURCE_FREE
                            break
                        else:
                            continue
                    else:
                        break
                else:
                    break
        return available, reason

