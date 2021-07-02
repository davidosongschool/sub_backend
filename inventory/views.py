from django.shortcuts import render
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Import stripe
import stripe
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET

# Get list of all products from Stripe Products
@api_view(['POST'])
def product_list(request):

    if request.method == 'POST':
        products = stripe.Product.list()
        return Response(products)


# Create A Product
@api_view(['POST'])
def create_product(request):

    print (request.data['name'])

    if request.method == 'POST':
        name = request.data['name']
        description = request.data['description']
        createdProduct = stripe.Product.create(name=name, description=description)
        return Response(createdProduct)

# Create A Price 
@api_view(['POST'])
def set_price(request):
    if request.method == 'POST':
        # Multiply price by 100 to get it in EUR 
        cost = request.data['price'] * 100 
        id = request.data['id']
        price = stripe.Price.create(
        product=id,
        unit_amount=cost,
        currency='EUR',  
        recurring={
        'interval': 'month',
        })
        return Response(price)

