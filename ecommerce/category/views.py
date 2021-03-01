from django.shortcuts import render
from category.models import Category
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.





def category(request):
    category = Category.objects.all()
    context = {
        'category':category
    }
    return render(request, 'category.html', context)


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
    context = {
        'products':products
    }
    return render(request, 'category_products.html', context)




