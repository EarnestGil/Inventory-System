from django import forms

from .models import Branch, Product, Window

class BranchForm(forms.ModelForm):
    pass

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        #fields = "__all__"
        exclude = ["thumbnail"]
