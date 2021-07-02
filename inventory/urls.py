from django.urls import path
from .views import product_list, set_price
from . import views

urlpatterns = [
    path('', views.product_list,),
    path('create_product/', views.create_product),
    path('set_price/', views.set_price)
]
