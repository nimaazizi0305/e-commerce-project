from django.db import models
from django.contrib.auth.models import User
from product.models import Product,Variation

# Create your models here.

class Pyament(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    payment_id=models.CharField(max_length=150)
    paymen_method=models.CharField(max_length=150)
    amount_paid=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    created_at=models.CharField(max_length=150)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    status=(
        ("New","New"),
        ("Accepted","Accepted"),
        ("Completed","Completed"),
        ("Cancelled","Cancelled")
    )

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    payment=models.ForeignKey(Pyament,models.SET_NULL,null=True,blank=True)
    order_number=models.CharField(max_length=200,null=True,blank=True)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=150)
    country=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    other_note=models.CharField(max_length=200)
    order_total=models.FloatField()
    quantity=models.IntegerField(blank=True,null=True)
    status=models.CharField(max_length=10,choices=status,default="New")
    ip=models.CharField(max_length=20,blank=True)
    is_oredered=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def full_address(self):
        return f"{self.country} - {self.city} - {self.address}"

    def __str__(self):
        return self.first_name


class OrderProduct(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    varation=models.ManyToManyField(Variation,blank=True)
    quantity=models.IntegerField()
    product_price=models.FloatField()
    ordered=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name


