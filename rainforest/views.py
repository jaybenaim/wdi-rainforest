
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render 
from datetime import datetime 
from rainforest.models import * 
from rainforest.forms import * 
from django import forms 
from django.urls import reverse



def root(request): 
    return HttpResponseRedirect('home')

def home(request): 
    products = Product.objects.all()
    context = { 
        "products": products
    }
    return render(request, 'index.html', context) 

def product_show(request, id):
    product = Product.objects.get(pk=id)
    review = Review.objects.filter(product=product)
    form = ReviewForm() 
    

    context = { 
        'product': product,
        'reviews': review, 
        'review_form': form, 
        'action': '/review/create'
    }

    return render(request, 'show_product.html', context) 

def product_new(request): 
    form = ProductForm() 
    context = { 
        'form': form,
        'action': '/product/create'
    }
    return render(request, 'product_form.html', context)

def product_create(request): 
    post = request.POST 
    form = ProductForm(post)
    form.save() 
    
    return HttpResponseRedirect('/')


def review_create(request): 
    review = ReviewForm(request.POST)
    product_id = request.POST['product'] 
    review.product = product_id
    review.save() 

    html = f'/product/{product_id}/show'
    return HttpResponseRedirect(html)


def delete_review(request, id): 
    review = Review.objects.get(pk=id) 
    review.delete() 
    # product_id = Product.objects.get(pk=id) 
    # html = f'/product/{product_id.id}/show'
    
    return HttpResponseRedirect('/')

