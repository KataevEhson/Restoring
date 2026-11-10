from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *



def home_page(request):
    context = { 
        'name': 'ehson',
        'age': 14,
        }
    return render(request, 'index.html', context)



def add_category(request):
    if request.method == "POST":
        Category.objects.create(
            name = request.POST["name"]
        )
        return redirect('add_dish')
    
    return render(request, "index.html")



def add_dish(request):
    if request.method == "POST":
        Dish.objects.create(
            name = request.POST["name"],
            category_id = request.POST["category_id"],
            price = request.POST["price"]
        )
        return redirect('table_number')
    
    return render(request, "index1.html")


def add_table_number(request):
    if request.method == "POST":
        Table.objects.create(
            number = request.POST["number"]
        )
        return redirect('home_pge')
    
    return render(request, "index2.html")



def home_page2(request):
    context = { 
        'name': 'Ehson',
        'age': 14,
        }
    return render(request, 'index3.html', context)

