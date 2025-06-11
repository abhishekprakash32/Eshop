from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        data = request.POST
        first_name = data.get('first_name')
        email = data.get('email')
        password = make_password(data.get('password'))

        # Save the customer
        customer = Customer(first_name=first_name, email=email, password=password)
        customer.save()

        return redirect('login')
