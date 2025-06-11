from django.contrib import admin
from store.models import Customer, Category, Products, Order

# Register your models to make them available in the admin panel
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Order)