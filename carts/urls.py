from django.urls import path
from .views import Cart,AddCartItem,remove_product_by_quantity,remove_product,checkout


urlpatterns=[
    path("",Cart,name="cart"),
    path("show-cart/",Cart, name="ShowCart"),
    path("add-cart/<int:product_id>",AddCartItem,name="AddCartItem"),
    path("remove-cart-by-quantity/<int:product_id>/<int:cart_item_id>", remove_product_by_quantity, name="RemoveCartItemByQuantity"),
    path("remove-product/<int:product_id>/<int:cart_item_id>", remove_product, name="RemoveCartItem"),
    path("checkout", checkout, name="checkout")

]