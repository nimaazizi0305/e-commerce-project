from django.urls import path
from .views import order,payments,order_complete,my_order,detail_order

urlpatterns=[
    path("place-order",order,name="place-order"),
    path("payments",payments,name="payments"),
    path("order-complete",order_complete,name="order_complete"),
    path("my-order/<str:username>",my_order,name="my_order"),
    path("my-order-detail/<str:order_id>",detail_order,name="detail_order")
]



