from django.urls import path

from . import views

urlpatterns = [
    path("catalog/", views.ProductListView.as_view(), name="product_list"),
]
