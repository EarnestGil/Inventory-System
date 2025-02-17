from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    path("new-product", views.ProductFormView.as_view(), name="new_product"),
]
