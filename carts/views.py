from Tools.i18n.msgfmt import usage
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from product.models import Product,Variation
from .models import Carts,CartItems
from django.contrib.auth.decorators import login_required
# Create your views here.

def Cart(request,total=0,quantity=0,cart_items=None):
    try:
        try:
            if request.user.is_authenticated:
                cart_items = CartItems.objects.filter(user=request.user, is_active=True)
            else:
                pass
            for cart_item in cart_items:
                total+=(cart_item.product.price * cart_item.quantity)
                quantity+=cart_item.quantity
        except TypeError:
            pass

    except ObjectDoesNotExist:
        pass # just Ignore

    context={
        "total":total,
        "quantity":quantity,
        "cart_items":cart_items
    }

    return render(request, "store/cart.html",context)


def cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart


def AddCartItem(request,product_id):
    product=Product.objects.get(id=product_id)
    product_vatation=[]

    if request.user.is_authenticated:
        if request.method=="POST":
            for item in request.POST:
                value=request.POST[item]
                try:
                    variation=Variation.objects.get(product=product,variation_value__iexact=value)
                    product_vatation.append(variation)
                except:
                    pass
        try:
            cart=Carts.objects.get(cart_id=cart_id(request),user=request.user.username) # cart means sabad kharid

        except Carts.DoesNotExist:
            cart=Carts.objects.create(cart_id=cart_id(request),user=request.user.username)
        cart.save()

        is_cart_item_exist=CartItems.objects.filter(product=product,user=request.user).exists()

        if is_cart_item_exist:
            cart_item=CartItems.objects.filter(product=product,user=request.user)

            exist_variaion_item=[]
            id=[]
            for item in cart_item:
                exist_variation=item.varation.all()
                exist_variaion_item.append(list(exist_variation))
                id.append(item.id)

            if product_vatation in exist_variaion_item:
                index=exist_variaion_item.index(product_vatation)
                item_id=id[index]
                item=CartItems.objects.get(product=product,id=item_id)
                item.quantity+=1
                item.save()
            else:
                item=CartItems.objects.create(product=product,quantity=1,user=request.user)

                if len(product_vatation)>0:
                    item.varation.clear()
                    item.varation.add(*product_vatation)

                # cart_item.quantity+=1
                item.save()

        else:
            cart_item=CartItems.objects.create(product=product,quantity=1,user=request.user)

            if len(product_vatation)>0:
                cart_item.varation.clear()
                cart_item.varation.add(*product_vatation)

            cart_item.save()
        return redirect("cart")
    else:
        if request.method == "POST":
            for item in request.POST:
                value = request.POST[item]
                try:
                    variation = Variation.objects.get(product=product, variation_value__iexact=value)
                    product_vatation.append(variation)
                except:
                    pass
        try:
            cart = Carts.objects.get(cart_id=cart_id(request), user=request.user.username)  # cart means sabad kharid

        except Carts.DoesNotExist:
            cart = Carts.objects.create(cart_id=cart_id(request), user=request.user.username)
        cart.save()

        is_cart_item_exist = CartItems.objects.filter(product=product, user=request.user).exists()

        if is_cart_item_exist:
            cart_item = CartItems.objects.filter(product=product, cart=cart, user=request.user)

            exist_variaion_item = []
            id = []
            for item in cart_item:
                exist_variation = item.varation.all()
                exist_variaion_item.append(list(exist_variation))
                id.append(item.id)

            if product_vatation in exist_variaion_item:
                index = exist_variaion_item.index(product_vatation)
                item_id = id[index]
                item = CartItems.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()
            else:
                item = CartItems.objects.create(product=product, quantity=1, cart=cart, user=request.user)

                if len(product_vatation) > 0:
                    item.varation.clear()
                    item.varation.add(*product_vatation)

                # cart_item.quantity+=1
                item.save()
        else:
            cart_item = CartItems.objects.create(product=product, cart=cart, quantity=1, user=request.user)

            if len(product_vatation) > 0:
                cart_item.varation.clear()
                cart_item.varation.add(*product_vatation)

            cart_item.save()
        return redirect("cart")



def remove_product_by_quantity(request,product_id,cart_item_id):
    product=get_object_or_404(Product,id=product_id) # we get product from Product table Who id = product_id
    try:
        cart_item=CartItems.objects.get(product=product,user=request.user,id=cart_item_id) # we get product from CartItems who product=product , cart=cart

        if cart_item.quantity>1:
            cart_item.quantity-=1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect("cart")


def remove_product(request,product_id,cart_item_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item=CartItems.objects.get(product=product,user=request.user,id=cart_item_id)
    cart_item.delete()
    return redirect("cart")


@login_required(login_url="login")
def checkout(request,total=0,quantity=0,cart_items=None):
    try:
        cart_items=CartItems.objects.filter(is_active=True,user=request.user)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)
            quantity+=cart_item.quantity

    except ObjectDoesNotExist:
        pass # just Ignore

    context={
        "total":total,
        "quantity":quantity,
        "cart_items":cart_items
    }

    return render(request, "order/checkout.html", context)






