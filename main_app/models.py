from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length = 100)
    petalnum = models.IntegerField()
    color = models.CharField(max_length = 100)
    origin = models.CharField(max_length = 100)

    def __str__(self):
        return self.name