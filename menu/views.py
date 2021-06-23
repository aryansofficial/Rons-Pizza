from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Menu

# Create your views here.
def menu(request):
    menu = Menu.objects.all()
    data = {
        'menuItems': menu
    }
    return render(request, 'menu/index.html', data)


def dish(request, id):
    item = get_object_or_404(Menu, pk=id)
    data = {
        'item': item
    }
    return render(request, 'menu/dish.html', data)


def search(request):
    if request.method == 'GET':
        query = request.GET['name']
    result = Menu.objects.filter(name__icontains=query)
    data = {
        'menuItems': result  
    }
    return render(request, 'menu/index.html', data)