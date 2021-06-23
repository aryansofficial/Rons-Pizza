from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from orders.models import Orders
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def kitchen(request):
    orders = Orders.objects.order_by('-created_date')
    data = {
        'orders': orders
    }
    return render(request, 'kitchen/Kitchen.html', data)

@login_required(login_url='login')
def update(request, id, status):
    order = Orders.objects.get(pk=id)
    if status == 'R':
        order.delete()
    else:
        order.progress = status
        order.save()
    return redirect('kitchen')
    # return HttpResponse(f'{id} {status}')

def dashboard(request):
    ready_orders = Orders.objects.filter(progress='C')
    cooking_orders = Orders.objects.filter(progress='P')
    # print(ready_orders)
    
    data = {
        'preapearing': cooking_orders,
        'completed': ready_orders
    }
    return render(request, 'kitchen/dashboard.html', data)