from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import DetailView,ListView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from .forms import RegisterForm
from django.views import generic
from django.contrib.auth.models import User,auth
from django.urls import reverse_lazy
from carts.views import cart_id
from carts.models import Carts,CartItems
from product.models import Product
from order.models import OrderProduct,Order
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
# Create your views here.


class Register(generic.CreateView):
    form_class = UserCreationForm
    template_name = "account/register.html"
    success_url = reverse_lazy("login")

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {'form':form})


def login(request):
    form=AuthenticationForm()
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            try:
                cart=Carts.objects.get(user=request.user.username)
                is_cart_item_exist=CartItems.objects.filter(user=request.user.username).exists()
                if is_cart_item_exist:
                    cart_item=CartItems.objects.filter(user=request.user.username)
                    for item in cart_item:
                        item.user=user
                        item.save()
            except:
                pass
            auth.login(request,user)
            return redirect("dashbord")
        else:
            return redirect("login")
    context={
        "form":form
    }
    return render(request,"account/signin.html",context)


# def register(request:HttpRequest):
#     if request.method == "POST":
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data.get("username")
#             messages.success(request,f"User {username} Created Now")
#             return redirect("login")
#     else:
#         form=UserCreationForm()
#     context={
#         "form":form
#     }
#     return render(request,"account/register.html",context)

@login_required(login_url="login")
def dashbord(request):
    username=request.user.username
    user_last_login=User.objects.get(username=username)
    orders=Order.objects.filter(user=request.user.id,is_oredered=True).order_by("-created_at")
    orders_count=orders.count()
    context={
        "username":username,
        "orders":orders,
        "orders_count":orders_count,
        "user_last_login":user_last_login
    }
    return render(request,"account/dashboard.html",context)


















