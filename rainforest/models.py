from django.db import models
from django.core import  validators
from django.core.exceptions import ValidationError


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False) 
    price = models.FloatField(null=False)
    
    def __str__(self): 
        return f'{self.name}'
        
class Review(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', default="")
    
    def __str__(self): 
        return f'{self.text}'
