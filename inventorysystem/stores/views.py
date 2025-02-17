from django.shortcuts import render

from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView

from django.urls import reverse_lazy

from .models import Product

from .forms import ProductForm

# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name = "product_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProductFormView(FormView):
    template_name = "stores/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
