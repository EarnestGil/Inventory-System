from django.shortcuts import render

from django.views import View
from django.views.generic.edit import FormView

from .forms import ProductForm

# Create your views here.
class ProductFormView(FormView):
    pass
