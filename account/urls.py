from django.urls import path
from .views import Register,dashbord,change_password

urlpatterns=[
    path("register",Register.as_view(),name="register"),
    path("dashbord",dashbord,name="dashbord"),
    path('change_password/', change_password, name='change_password'),
]






