from django.shortcuts import render
from store.models.orders import Order
from django.views import View

class OrderView(View):
    def get(self, request):
        customer_id = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer_id)
        return render(request, 'orders.html', {'orders': orders})
