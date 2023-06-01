from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'digital', 'image')


class CouponForm(forms.Form):
    code = forms.CharField(max_length=50)

class CustomerCreationForm(UserCreationForm):
    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Customer
        fields = ('name', 'email', 'password1', 'password2')