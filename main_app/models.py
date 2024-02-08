from django.db import models
from datetime import date

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Flower(models.Model):
    name = models.CharField(max_length = 100)
    petalnum = models.IntegerField()
    color = models.CharField(max_length = 100)
    origin = models.CharField(max_length = 100)
    customers = models.ManyToManyField(Customer, related_name='flowers')

    def __str__(self):
        return self.name    
    def hydrate_for_today(self):
        return self.hydrate_set.filter(date = date.today()).count()>=1
    
Hydrate_time = [
    ('M','Morning'),
    ('N','Night')
]
Hydrate_type = [
    ('SP','Spray'),
    ('SH', 'Shower'),
    ('SO', 'Soak')
]
class Hydrate(models.Model):
    date = models.DateField('Hydrate date')
    time = models.CharField('Hydrate time', max_length=2, choices=Hydrate_time, default=Hydrate_time[0])
    type = models.CharField('Hydrate type',max_length=2, choices=Hydrate_type,default=Hydrate_type[1])
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.get_type_display()} {self.flower} at {self.time}'
    
    class Meta:
        ordering = ['-date']