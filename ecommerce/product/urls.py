from django.urls import path
from .views import *


urlpatterns = [
    path('',index, name='index'),
    path('category/<slug>/', category_detail, name='category_detail'),
    path('category/product/<slug>/', product_detail, name='product_detail'),
]

