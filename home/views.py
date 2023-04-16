from django.shortcuts import render
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,BaseUserManager
from product.models import Product

# Create your views here.

def home(request):
    products=Product.objects.all().filter(is_active=True)
    context={
        "products":products,
    }
    return render(request, "home.html",context)


