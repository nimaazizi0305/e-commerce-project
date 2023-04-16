from django.shortcuts import render, get_object_or_404,HttpResponse
from .models import Product,Review,ProductGallery
from category.models import Category
from django.views.generic import ListView,DetailView
from carts.models import CartItems,Carts
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q
from order.models import OrderProduct

# Create your views here.

def store(request,category_slug=None):
    all_categories=Category.objects.all().filter(is_active=True)

    if category_slug !=None:
        categories=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(is_active=True,category=categories)
        paginetor = Paginator(products, 2)
        page = request.GET.get("page")
        paged_products = paginetor.get_page(page)
        product_count = Product.objects.filter(is_active=True,category=categories).count()
    else:
        products=Product.objects.all().filter(is_active=True)
        paginetor=Paginator(products,2)
        page=request.GET.get("page")
        paged_products=paginetor.get_page(page)
        product_count=Product.objects.count()

    context={
        "products":paged_products,
        "product_count":product_count,
        "all_categories":all_categories
    }
    return render(request, "store/store.html",context)


class ProductDetial(DetailView):
    template_name = "store/product-detail.html"
    model = Product
    context_object_name = "product"

    def get_context_data(self,*args,**kwargs):
        context = super(ProductDetial, self).get_context_data(*args, **kwargs)
        return context


def Search(request):
    all_categories=Category.objects.all().filter(is_active=True)

    if "keyword" in request.GET:
        keyword=request.GET["keyword"]
        if keyword: # keyword is not blank
            product_count = Product.objects.filter(is_active=True and Q(name__icontains=keyword) | Q(description__icontains=keyword)).count()
            products=Product.objects.filter(is_active=True and Q(name__icontains=keyword) | Q(description__icontains=keyword)).order_by("-created_date")

    conext={
        "products":products,
        "all_categories":all_categories,
        "product_count": product_count,
    }
    return render(request,"store/store.html",conext)


def sernd_review(request,slug):
    product = Product.objects.get(slug=slug)
    user_buy=OrderProduct.objects.filter(product=product,user=request.user).exists()
    if request.method == "POST":
        user = request.user
        product = Product.objects.get(slug=slug)
        subject = request.POST["subject"]
        review = request.POST["review"]
        ip = request.META.get("REMOTE_ADDR")
        new_review = Review.objects.create(user=user, subject=subject, review=review, product=product, ip=ip)
        new_review.save()
        context = {
            "product": product,
            "user_buy":user_buy
        }

    else:
        product = Product.objects.get(slug=slug)

        context = {
            "product": product,
            "user_buy":user_buy
        }

    return render(request,"store/review.html",context)


