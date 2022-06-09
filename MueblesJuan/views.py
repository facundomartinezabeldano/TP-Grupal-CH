from django.shortcuts import render


def home(request):
    template = 'index.html'
    context_payload = {}
    return render(request=request, template_name=template, context=context_payload)


def faq(request):
    template = 'faq.html'
    context_payload = {}
    return render(request=request, template_name=template, context=context_payload)
