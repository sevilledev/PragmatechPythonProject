from django.shortcuts import render
<<<<<<< HEAD
from category.models import Category
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import HttpResponse, JsonResponse
import json
=======
from category.models import *

>>>>>>> c440e2c153e5286d497f9eb4be5b48029f9a9fba
# Create your views here.



def category(request):
    category = Category.objects.all()
    context = {
        'category':category
    }
    return render(request, 'category.html', context)

<<<<<<< HEAD

@csrf_exempt
def category_products(request, slug):
    products = Category.products_in_category(slug)
################ POST ##############
    if request.method == "POST":
        data2 = request.POST['q']
        url = 'https://api.teammers.com/project/packets/{}/?format=json'.format(data2)
        a = requests.get(url)
        print(a.text)
        js = json.loads(a.text)
        return JsonResponse(js)
    ########### GET ################
    try:
        data = request.GET.get('q')
        print(request.GET)
        url = '{}'.format(data)
        a = requests.get(url)
        return HttpResponse(a.text)
    except:
        pass
=======
def category_subcategories(request, cat_slug):
    subcategories = Category.subcategories_in_category(cat_slug)
>>>>>>> c440e2c153e5286d497f9eb4be5b48029f9a9fba
    context = {
        'subcategories':subcategories
    }
<<<<<<< HEAD
    return render(request, 'category_products.html', context)



=======
    return render(request, 'category_subcategories.html', context)

def subcategory_brands(request, cat_slug, subcat_slug):
    brands = SubCategory.brands_in_subcategory(subcat_slug)
    context = {
        'brands':brands
    }
    return render(request, 'subcategory_brands.html', context)
>>>>>>> c440e2c153e5286d497f9eb4be5b48029f9a9fba

