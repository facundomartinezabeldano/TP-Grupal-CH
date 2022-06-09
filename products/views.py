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
    payload = {'products': res}
    print(res)
    return render(request=request, template_name=view, context=payload)


def order(request):
    template = 'order.html'
    my_form = OrderForm(request.POST)
    if my_form.is_valid():
        payload = my_form.cleaned_data
        order = Orden(
            name=payload['name'],
            email=payload['email'],
            producto=payload['product'],
            message=payload['message'],
        )
        order.save()
        template = 'success.html'
        return render(request=request, template_name=template, context={})
    else:
        my_form = OrderForm()
        return render(request=request, template_name=template, context={'form': my_form})


def success(request):
    template = 'success.html'
    return render(request=request, template_name=template, context={})
