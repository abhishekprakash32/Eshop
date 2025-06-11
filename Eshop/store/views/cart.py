from django.shortcuts import render, redirect
from django.views import View
from store.models.products import Products


class Cart(View):
    def get(self, request):
        # Retrieve cart data from the session
        cart = request.session.get('cart', {})
        product_ids = list(cart.keys())

        # Fetch product details for the items in the cart
        products = Products.objects.filter(id__in=product_ids)

        # Prepare context for the template
        context = {
            'products': products,
            'cart': {product.id: {'quantity': quantity, 'product': product} for product, quantity in zip(products, cart.values())},
        }
        return render(request, 'cart.html', context)

    def post(self, request):
        # Handle "Add to Cart" functionality
        product_id = request.POST.get('product')
        if not product_id:
            return redirect('cart')  # Redirect back if product_id is missing

        cart = request.session.get('cart', {})

        # Update the cart quantity or add the product
        if product_id in cart:
            cart[product_id] += 1
        else:
            cart[product_id] = 1

        request.session['cart'] = cart
        return redirect('cart')
