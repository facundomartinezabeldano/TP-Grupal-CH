from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from itertools import chain
from .forms import *

# Create your views here.


def products(request):
    view = 'products.html'
    sillas = Silla.objects.all()
    mesas = Mesa.objects.all()
    escritorios = Escritorio.objects.all()
    sillones = Sillon.objects.all()
    res = list(chain(sillas, mesas, escritorios, sillones))
    payload = {'products': res,
               'sillas': sillas,
               'mesas': mesas,
               'escritorios': escritorios,
               'sillones': sillones
               }
    print(res)
    return render(request=request, template_name=view, context=payload)


def order(request):
    template = 'order.html'
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        product_name = request.POST['product']
        message = request.POST['message']
        orden = Orden(
            name=name,
            email=email,
            product=product_name,
            message=message
        )
        orden.save()
    return render(request=request, template_name=template, context={})


def success(request):
    pass
