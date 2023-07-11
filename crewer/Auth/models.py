from django.db import models
from django.contrib.auth.models import AbstractUser
from TaskManager.models import Skill

# Create your models here.
class User(AbstractUser):
    skills = models.ManyToManyField(Skill, blank=True, null=True)

