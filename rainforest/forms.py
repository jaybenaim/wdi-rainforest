from django.db import models
from django.forms import ModelForm 
from rainforest.models import * 
from django import forms 

class ProductForm(ModelForm): 
    class Meta: 
        model = Product 
        fields = ['name', 'description', 'price']

class ReviewForm(ModelForm): 
    class Meta: 
        model = Review 
        fields = ['text', 'product']
        