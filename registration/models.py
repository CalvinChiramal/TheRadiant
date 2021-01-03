from django.db import models

# Create your models here.
class Events(models.Model):
    eventName = models.CharField(max_length=15, blank=False)
    eventDesc = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.eventName

class Register(models.Model):
    name = models.CharField(max_length=30, blank=False)
    age = models.IntegerField(blank=False)
    college = models.CharField(max_length=30, blank=False, default='college')
    dept = models.CharField(max_length=15, blank=False, default='dept')
    eventName = models.CharField(max_length=50, blank=False, default='event')

    def __str__(self):
        return self.name