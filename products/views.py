from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def products(request):
    view = 'products.html'
    context = {}
    return render(request=request, template_name=view, context=context)
