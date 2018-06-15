from django.contrib import admin
from django.contrib.auth.models import User

from .models import Dish, Category, Cart, Location

@admin.register(Dish) 
class DishAdmin(admin.ModelAdmin):
    fields = ("dish_name", "description", "price", "creator")
    list_display = ["dish_name"]
    search_fields = ("dish_name", "category")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ("slug", "dish")
    list_display = ["slug"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin): 
    fields = ("owner","items")


admin.site.register(Location)
