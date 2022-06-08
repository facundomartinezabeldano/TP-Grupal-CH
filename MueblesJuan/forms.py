from django import forms


class OrderForm (forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField
    product = forms.ChoiceField(
        choices=['Silla', 'Sillon', 'Escritorio', 'Mesa'])
    message = forms.CharField(max_length=300)
