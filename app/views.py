from django.shortcuts import render, HttpResponse

from cart.cart import Cart


# Create your views here.

def home(request):
    cart = Cart(request)
    return render(request, 'app/home.html')