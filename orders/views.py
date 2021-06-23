from django.shortcuts import render, redirect
from .models import Orders
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def add(request):
    # if request.method == 'POST':
    quantity = request.GET['quantity']
    item = request.GET['item_id']
        
    order = Orders(
        quantity=quantity,
        dish_id=item
    )

    order.save()
    messages.success(request, f'Order placed Order ID: {order.id}')
    return redirect(f'dish/{item}')
    # return HttpResponse('Home')