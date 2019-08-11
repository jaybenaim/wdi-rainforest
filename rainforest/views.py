
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect 
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
    product_id = Product.objects.get(pk=id)
    review = Review.objects.filter(product=product_id).order_by('date')
    form = ReviewForm() 
    

    context = { 
        'product': product_id,
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

def edit_product(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'GET': 
        form = ProductForm(instance=product)
        context = { 'form': form, 'product': product }
        return render(request, 'edit_product.html', context)
    elif request.method == 'POST': 
        form = ProductForm(instance=product)
        updated_product = form.save() 
        return redirect(reverse('show_product', args=[product.id]))

def delete_product(request, id): 
    product = Product.objects.get(pk=id)
    product.delete() 
    return redirect('/')

def review_create(request): 
    review = ReviewForm(request.POST)
    product_id = request.POST['product'] 
    review.product = product_id
    review.save() 

    html = f'/product/{product_id}/show'
    return HttpResponseRedirect(html)


def edit_review(request, id): 
    # 'review/<int:id>/update'
    review = Review.objects.get(pk=id)
    product_id = review.product.id
    review_edit_form = ReviewForm(instance=review) 
    context = { 
        'review_edit_form': review_edit_form,  
        'action': f"/review/{review.pk}/update"
    } 
    return render(request, 'review_edit_form.html' , context)

def update_review(request, id): 
    review = Review.objects.get(pk=id)
    form = ReviewForm(request.POST, instance=review) 
    form.save() 
    
    product_id = request.POST['product'] 
    html = f'/product/{product_id}/show'
    return HttpResponseRedirect(html)
  

def delete_review(request, id): 
    review = Review.objects.get(pk=id) 
    review.delete() 
  
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))




