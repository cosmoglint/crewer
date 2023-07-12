from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    skills = models.ManyToManyField("TaskManager.Skill", blank=True)
    role = models.PositiveSmallIntegerField(choices=settings.ROLE_CHOICES, blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     if self.pk is not None:
    #         orig = User.objects.get(pk=self.pk)
    #         if orig.pass != self.f1:
    #     super().save(*args, **kwargs)

