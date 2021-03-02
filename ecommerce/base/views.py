from django.shortcuts import render
from category.models import Category
# Create your views here.

def index(request):
    category = Category.objects.prefetch_related('q').all()


    context = {
        'category':category,
    }
    return render(request,'index.html',context)