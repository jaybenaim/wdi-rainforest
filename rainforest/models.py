from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(null=False) 
    price = models.FloatField(null=False)
    
    def __str__(self): 
        return f'{self.name}'
        
class Review(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)
    product_id = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    
    def __str__(self): 
        return f'{self.text}'
