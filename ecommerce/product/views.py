from django.shortcuts import render
from .models import *

# Create your views here.

def product(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'user': request.user
    }
    return render(request, 'products/product.html', context)