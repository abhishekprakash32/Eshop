from django.shortcuts import render, redirect
from store.models.category import Category
from store.models.products import Products
from django.views import View

class Index(View):
    def get(self, request):
        products = Products.get_all_products()
        categories = Category.get_all_categories()
        context = {'products': products, 'categories': categories}
        return render(request, 'index.html', context)
