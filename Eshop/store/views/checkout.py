from django.shortcuts import render
from django.views import View
from store.models.products import Products  # Importing the Products model
from store.models.orders import Order  # Importing the Order model
from store.models.customer import Customer  # Importing the Customer model

class CheckOut(View):
    def get(self, request):
        # Retrieve the cart data from session
        cart = request.session.get('cart', {})
        product_ids = list(cart.keys())  # Extract product IDs from the cart

        # Fetch product details for the products in the cart
        products = Products.objects.filter(id__in=product_ids)

        # Create a list of products and their quantities to pass to the template
        cart_with_products = [
            {'product': product, 'quantity': cart.get(str(product.id))}
            for product in products
        ]

        return render(request, 'checkout.html', {'cart': cart_with_products})

    def post(self, request):
        # Handle the checkout process when the form is submitted
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart', {})
        product_ids = list(cart.keys())
        products = Products.objects.filter(id__in=product_ids)

        # Create an Order for each product in the cart
        for product in products:
            order = Order(
                product=product,
                customer=Customer(id=customer),
                quantity=cart.get(str(product.id)),
                price=product.price,
                address=address,
                phone=phone
            )
            order.save()

        # Clear the cart after checkout
        request.session['cart'] = {}

        # Pass the order details to the checkout template
        cart_with_products = [
            {'product': product, 'quantity': cart.get(str(product.id))}
            for product in products
        ]

        return render(request, 'checkout.html', {
            'cart': cart_with_products,
            'address': address,
            'phone': phone
        })
