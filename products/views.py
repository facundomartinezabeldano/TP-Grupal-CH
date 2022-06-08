from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from itertools import chain

# Create your views here.


def products(request):
    view = 'products.html'
    sillas = Silla.objects.all()
    mesas = Mesa.objects.all()
    escritorios = Escritorio.objects.all()
    sillones = Sillon.objects.all()
    res = list(chain(sillas, mesas, escritorios, sillones))
    payload = {'products': res}
    print(res)
    return render(request=request, template_name=view, context=payload)