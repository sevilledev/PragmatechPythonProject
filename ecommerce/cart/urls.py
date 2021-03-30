from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', cart_products, name='cart_products'),
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('change_quantity/<int:id>/<int:qyt>/', change_quantity, name='change_quantity'),
    path('confirm_cart/', confirm_cart, name='confirm_cart'),
]
