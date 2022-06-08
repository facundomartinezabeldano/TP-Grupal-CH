from django.shortcuts import render
from .forms import OrderForm


def home(request):
    template = 'index.html'
    context_payload = {}
    return render(request=request, template_name=template, context=context_payload)


def faq(request):
    template = 'faq.html'
    context_payload = {}
    return render(request=request, template_name=template, context=context_payload)


def order(request):
    template = 'order.html'
    if request.method == 'POST':
        orden = OrderForm()
    return render(request=request, template_name=template, context={})
