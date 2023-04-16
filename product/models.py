from django.db import models
from category.models import Category
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(unique=True)
    price=models.IntegerField()
    description=models.TextField(blank=True,max_length=500)
    image=models.ImageField(upload_to="photos/product")
    is_active=models.BooleanField(default=True)
    stock=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    published_date=models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)

    def review_product(self):
        product=Product.objects.get(name=self.name)
        review_product=Review.objects.filter(product=product)
        return review_product

    def product_gallery(self):
        product=Product.objects.get(name=self.name)
        gallery=ProductGallery.objects.filter(product=product)
        return gallery

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if self.is_active==False:
            self.published_date=None
        else:
            self.published_date=timezone.now()
        super().save(*args,**kwargs)

class VartiationManager(models.Manager):
    def colors(self):
        return super(VartiationManager,self).filter(variation_category="COLOR",is_active=True)

    def sizes(self):
        return super(VartiationManager,self).filter(variation_category="SIZE",is_active=True)


Variation_choices={
    ("COLOR","color"),
    ("SIZE","size")
}

class Variation(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category=models.CharField(max_length=200,choices=Variation_choices)
    variation_value=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now=True)
    objects=VartiationManager()

    def __str__(self):
        return self.variation_value


class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100)
    review=models.TextField(max_length=500)
    ip=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class ProductGallery(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image_produtc=models.ImageField(upload_to="photos/product_gallery",max_length=520)

    def __str__(self):
        return self.product.name





