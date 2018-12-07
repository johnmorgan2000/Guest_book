from django.db import models


class Guest(models.Model):
    name = models.TextField()
    message = models.TextField()
    date = models.DateField()
