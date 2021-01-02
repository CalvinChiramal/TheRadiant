from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=30, blank=False)
    age = models.IntegerField(blank=False)
    eventName = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name