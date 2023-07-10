from django.db import models

class Project(models.Model):
    name = models.CharField(max_lengt=150)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()