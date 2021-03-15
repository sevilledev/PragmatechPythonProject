from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_to_wishlist/<int:id>/',add_to_wishlist,name='add_to_wishlist'),
]