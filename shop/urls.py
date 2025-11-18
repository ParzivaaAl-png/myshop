# shop/urls.py  (или myshop/urls.py — там, где у тебя корневой urls)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("products.urls", namespace="products")),  # <--- важно: namespace = 'products'
]
