from category.models import Category
from django.shortcuts import render

def category_in_header(request):
    all_category=Category.objects.all().filter(is_active=True) #all_category is list
    return dict(all_category=all_category) # we convert all_category list to dictionary

