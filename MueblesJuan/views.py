from django.shortcuts import render
from .forms import OrderForm
from products.models import Orden


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

    my_form = OrderForm(request.POST)
    if my_form.is_valid:
        payload = my_form.cleaned_data
        order = Orden(
            name=payload['name'],
            email=payload['email'],
            producto=payload['product'],
            message=payload['message'],
        )
        order.save()
    else:
        my_form = OrderForm()

    return render(request=request, template_name=template, context=my_form)
