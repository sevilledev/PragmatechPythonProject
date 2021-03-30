from django.shortcuts import render, redirect
from .models import Product, CartProduct, Cart

# Create your views here.

def cart_products(request):
    products = []
    total = 0
    for product in request.session['cart']:
        p_data = dict(product)
        id = p_data['id']
        quantity = p_data['quantity']
        obj = Product.objects.get(id=id)
        products.append((obj,quantity))
        if obj.product_discount :
            total += obj.product_discount_price * quantity
        else :
            total += obj.product_price * quantity
    context = {
        'products':products,
        'total':total
    }
    return render(request, 'cart_products.html', context)

def add_to_cart(request, id):
    if request.method == "POST":
        if not request.session.get('cart'):
            request.session['cart'] = list()
        else:
            request.session['cart'] = list(request.session['cart'])
    products = next((item for item in request.session['cart'] if item['id']==id),False)
    add_product = {
        'id':id,
        'quantity':1
    }
    if not products:
        request.session['cart'].append(add_product)
        request.session.modifier = True

    return redirect('cart_products')

def change_quantity(request, id, qyt):
    if request.method == 'POST':
        new_session_data = []
        for product in request.session['cart']:
            p_data = dict(product)
            p_id = p_data['id']
            if p_id == id:
                p_data['quantity'] = qyt
            new_session_data.append(p_data)
        request.session['cart'] = new_session_data
        print(new_session_data)
    return redirect('cart_products')

    
def confirm_cart(request):
    products = []
    for product in request.session['cart']:
        id = product['id']
        quantity = product['quantity']
        obj = Product.objects.get(id=id)
        products.append((obj,quantity))
    context = {
        'products':products,
    }
    if request.method == 'GET':
        cart_products = []
        for product in products:
            p_data = list(product)
            print(p_data)
            cart_product = CartProduct(product=p_data[0], quantity=p_data[1])
            cart_product.save()
            cart_products.append(cart_product)
        cart = Cart()
        cart.save()
        for cart_product in cart_products:
            cart.products.add(cart_product)
        try :
            cart.save()
        except :
            cart.delete()
        
    return render(request, 'confirm_cart.html', context)