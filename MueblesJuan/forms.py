from django import forms


class OrderForm (forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField
    product = forms.CharField()
    message = forms.CharField(max_length=300)
