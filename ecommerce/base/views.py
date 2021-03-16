from django.shortcuts import render, redirect
from category.models import *
from staticpage.models import *
from product.models import Product
from django.http import JsonResponse

# Create your views here.

def index(request):
    categories = Category.objects.prefetch_related('sub_categories').all()
    sliders = Slider.objects.all()
    #request.session['test'] = 10
    print(request.session.items())
    products = Product.objects.all()[:10]
    context = {
        'categories':categories,
        'sliders':sliders,
        'pro':products, 
    }
    return render(request,'index.html',context)

def add_to_wishlist(request,id):
    if request.method == "POST":
        if not request.session.get('wishlist'):
            request.session['wishlist'] = list()
        else:
            request.session['wishlist'] = list(request.session['wishlist'])
        items = next((item for item in request.session['wishlist'] if item['id']==id),False)
    add_data = {
        'id':id,
    }
    if not items:
        request.session['wishlist'].append(add_data)
        request.session.modifier = True
    return redirect('index')


def remove_wishlist(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        for i in request.session['wishlist']:
            if str(i['id']) == id:
                i.clear()
                
        while {} in request.session['wishlist']:
            request.session['wishlist'].remove({})
        if not request.session['wishlist']:
            del request.session['wishlist']
    try:
        request.session['wishlist'] = list(request.session['wishlist'])
    except:
        pass
    request.session.modifier = True
    return JsonResponse({'status':'ok'})


