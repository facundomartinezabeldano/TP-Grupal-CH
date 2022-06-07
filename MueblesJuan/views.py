from django.shortcuts import render


def home(request):
    template = 'products.html'
    return render(request=request, template_name=template)


def faq(request):
    template = 'faq.html'
    return render(request=request, template_name=template)
