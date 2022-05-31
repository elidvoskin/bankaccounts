from django.db import models

class Checking(models.Model):
    name = models.CharField(max_length=50)
    balance = models.FloatField()

    def __str__(self):
            return self.name

