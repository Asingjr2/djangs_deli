from django.contrib.auth.models import User

from rest_framework import serializers

from store.models import Dish, Category, Cart, Location


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = { "password" : { "write_only": True, "required": True}}

    # Overriding builtin create method that is automatically assocaited with post to include different data to be pased to the user.objects.create method.  
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ("id","dish_name", "description","price", "category", "creator")
        lookup_field = "pk"


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Category
        fields = ("slug","dish")
        lookup_field = "slug"


class CartSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Cart
        fields = ("id", "owner","items",)
        lookup_field = "id"
        extra_kwargs = { "items": {"many": True}}


class LocationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Location
        fields = ("id", "state", "store_name", "address", "established", "best_dish", "region")
   