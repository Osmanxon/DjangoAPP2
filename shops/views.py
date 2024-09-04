from django.shortcuts import render
from django.views import View
from .models import Products

# Create your views here.

class HomePageView(View):
    def get(self, request):
        return render(request, "shops/home.html")

class ProductView(View):
    def get(self, request):
        products = Products.objects.all()
        context = {
            "products": products
        }
        return render(request, "shops/products.html", context=context)


class ProductsDetailView(View):
    def get(self, request, id):
        product = Products.objects.get(id=id)
        context = {
            "products":product
        }
        return render(request, "shops/product_detail.html", context)