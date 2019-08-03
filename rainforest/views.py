
from django.http import HttpResponse, HttpResponseRedirect
from rainforest.models import * 
from django.shortcuts import render 


def root(request): 
    return HttpResponseRedirect('home')

def home(request): 
    products = Product.objects.all()
    context = { 
        "products": products
    }
    return render(request, 'index.html', context) 

def product_show(request, id):
    product_id = Product.objects.get(pk=id)
    review_id = Review.objects.filter(product_id=id)

    context = { 
        'product': product_id,
        'reviews': review_id
    }

    return render(request, 'show_product.html', context) 
