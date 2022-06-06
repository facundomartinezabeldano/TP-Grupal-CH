from django.shortcuts import render


def home(request):
    template = 'products/index_template_0.html'
    return render(request=request, template_name=template)


def faq(request):
    template = 'products/faq.html'
    return render(request=request, template_name=template)
