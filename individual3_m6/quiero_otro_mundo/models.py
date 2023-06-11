from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, null=False, blank=True)
    name = models.CharField(max_length=50, null=False, blank=True)
    surname = models.CharField(max_length=50, null=False, blank=True)
    email  = models.EmailField(null=False, blank=True)
    address = models.CharField(max_length=50, null=False, blank=True)
    city = models.CharField(max_length=50, null=False, blank=True)

    def __str__(self):
        return self.username