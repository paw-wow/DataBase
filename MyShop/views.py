from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .models import Product
from django.views.decorators.http import require_POST
from cart.forms import CartAddProductForm

class ProductView(View):
    """Список товаров"""
    def get(self, request):
        product = Product.objects.all()
        return render(request, "shop/index.html", {"product_list": product})

class Product_detail(View):
    """Сам товар"""
    def get(self, request, slug):
        product = Product.objects.get(url=slug)
        count = Product.objects.get(url=slug).count
        cart_product_form = CartAddProductForm()
        return render(request, "shop/single-product.html", {'product': product, 'cart_product_form': cart_product_form, 'count': count})