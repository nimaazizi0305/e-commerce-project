from django.urls import path
from .views import store,ProductDetial,Search,sernd_review

urlpatterns=[
    path("store",store,name="store"),
    path("category/<slug:category_slug>",store,name="product_by_category"),
    path("<slug:slug>",ProductDetial.as_view(), name="product-detail"),
    path("search/",Search,name="search"),
    path("review/<str:slug>",sernd_review,name="send_review")
]