from django import forms
from django.utils.translation import override

PRODUCT_QUALITY_CHOICES = [(i,str(i)) for i in range(1,21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUALITY_CHOICES, coerce=int)
