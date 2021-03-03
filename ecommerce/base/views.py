from django.shortcuts import render
from category.models import Category

# Create your views here.

def index(request):
    categories = Category.objects.prefetch_related('sub_categories').all()
    context = {
        'categories':categories,
    }
    return render(request,'index.html',context)