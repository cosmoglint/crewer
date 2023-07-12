from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __unicode__(self):
        return u'%s' % (self.name)

    def __str__(self):
        return self.name