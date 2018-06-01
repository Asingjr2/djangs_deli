from django.contrib import admin
from django.contrib.auth.models import User

from .models import Dish, Category

@admin.register(Dish) 
class DishAdmin(admin.ModelAdmin):
    fields = ("dish_name", "description",  "spice", "creator")
    list_display = ["dish_name"]
    search_fields = ("dish_name", "category")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ("slug", "dish")
    list_display = ["slug"]