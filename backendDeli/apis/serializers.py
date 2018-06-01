from django.contrib.auth.models import User

from rest_framework import serializers

from store.models import Dish, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = { "password" : { "write_only": True, "required": True}}

    # Overriding builtin create method that is automatically assocaited with post to include different data to be pased to the user.objects.create method.  
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ("id","dish_name", "description", "spice", "creator")


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Category
        fields = ("slug","dish")
        lookup_field = "slug"


