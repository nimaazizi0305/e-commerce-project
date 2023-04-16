from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Order, OrderProduct
from carts.models import CartItems, Carts
import datetime
from product.models import Product
from datetime import datetime


# Create your views here.

def order(request, total=0, quantity=0):
    cart_items = CartItems.objects.filter(user=request.user, is_active=True)
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        phone_number = request.POST["phone_number"]
        email = request.POST["email"]
        country = request.POST["country"]
        city = request.POST["city"]
        address = request.POST["address"]
        other_note = request.POST["other_note"]
        created = datetime.now()
        ip = request.META.get("REMOTE_ADDR")
        now = datetime.now()
        d = int(now.day)
        m = int(now.month)
        y = int(now.year)
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        Order.objects.create(user=request.user, first_name=first_name, ip=ip, other_note=other_note, quantity=quantity,
                             address=address,
                             city=city, country=country, email=email, phone_number=phone_number, last_name=last_name,
                             order_total=total, created_at=created,order_number=current_time)
        return redirect("payments")

    return render(request, "order/checkout.html", {})


def payments(request, total=0, quantity=0):
    cart_items = CartItems.objects.filter(user=request.user, is_active=True)
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

    order = Order.objects.filter(user=request.user, is_oredered=False,status="New").exists()
    if order:
        order = Order.objects.get(user=request.user, is_oredered=False,status="New")
        order.is_oredered = True
        order.status="Completed"
        order.save()

        for item in cart_items:
            order_product = OrderProduct()
            order_product.order_id = order.id
            order_product.user_id = request.user.id
            order_product.product_id = item.product_id
            order_product.quantity = item.quantity
            order_product.product_price = item.product.price
            order_product.ordered = True
            order_product.save()

            cart_item1 = CartItems.objects.get(id=item.id)
            product_varaition = cart_item1.varation.all()
            order_product = OrderProduct.objects.get(id=order_product.id)
            order_product.varation.set(product_varaition)
            order_product.save()

            product = Product.objects.get(id=item.product.id)
            product.stock -= item.quantity
            product.save()

        CartItems.objects.filter(user=request.user).delete()
        Carts.objects.filter(user=request.user).delete()
    else:
        pass

    context = {
        "order": order,
        "cart_items": cart_items,
        "total": total,
        "quantity": quantity
    }
    return render(request, "order/payments.html", context)


def order_complete(request):
    order = Order.objects.get(user=request.user, is_oredered=False)
    return render(request, "order/order_complete.html")


def my_order(request,username):
    user=User.objects.get(username=username)
    user_order=Order.objects.filter(user=user,is_oredered=True, status="Completed").order_by("-created_at")
    context={
    "user":user,
    "user_order":user_order
    }

    return render(request,"order/my_order.html",context)

def detail_order(request,order_id):
    order=Order.objects.get(order_number=order_id)
    product_order=OrderProduct.objects.filter(order=order)
    context={
        "product_order":product_order,
        "order":order
    }
    return render(request,"order/my_detail_order.html",context)



