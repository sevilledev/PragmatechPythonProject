from django.shortcuts import render
from category.models import *
from staticpage.models import *

# Create your views here.

def index(request):
    categories = Category.objects.prefetch_related('sub_categories').all()
    sliders = Slider.objects.all()
    context = {
        'categories':categories,
        'sliders':sliders 
    }
    return render(request,'index.html',context)