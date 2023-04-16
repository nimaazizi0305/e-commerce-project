from django.db import models
from product.models import Product,Variation
from django.contrib.auth.models import User

# Create your models here.

class Carts(models.Model):
    cart_id=models.CharField(max_length=200,blank=True)
    date_add=models.DateTimeField(auto_now_add=True)
    user=models.CharField(max_length=200,blank=True,null=True)


    def __str__(self):
        return self.cart_id

class CartItems(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    varation=models.ManyToManyField(Variation,blank=True)
    cart=models.ForeignKey(Carts,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField()
    is_active=models.BooleanField(default=True)

    def total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name

