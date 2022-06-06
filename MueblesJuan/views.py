from django.shortcuts import render


def home(request):
    return render(request=request, template_name='index.html')


def faq(request):
    return
