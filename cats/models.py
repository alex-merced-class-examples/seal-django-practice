from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    legs = models.IntegerField(default=4)
    
    
## Mongo Cat.create()
## Django Cat.objects.create()