from django.contrib.auth.models import User

from rest_framework import viewsets, status, generics
from rest_framework.authentication import  TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import list_route



from rest_framework.generics import GenericAPIView


from apis.serializers import UserSerializer, DishSerializer, CategorySerializer, CartSerializer, LocationSerializer
from .models import Dish, Category, Cart, Location


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    # authentication_classes = ( TokenAuthentication, SessionAuthentication )
    # permission_classes = (IsAuthenticated,)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    authentication_classes = ( TokenAuthentication, SessionAuthentication )
    permission_classes = (IsAuthenticated,)


class CartViewSet(viewsets.ModelViewSet): 
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # authentication_classes = ( TokenAuthentication, SessionAuthentication )
    # permission_classes = (IsAuthenticated,)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CartItemListViewSet(generics.ListAPIView):
    serializer_class = DishSerializer

    def get_queryset(self): 
        cartID = self.kwargs['cartID']
        return Dish.objects.filter(items__id=cartID)


class testviewset(generics.UpdateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    lookup_field = "pk"

    # def get_queryset(self): 
        # pk = self.kwargs['pk']


# # Creating custom user method to get token.  Can be done different ways
# # http://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
# Method returns JWT token for use if user login information is valid
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        user = User.objects.get(id=token.user_id)
        serializer = UserSerializer(user, many= False)
        return Response({
            "token": token.key, "user": serializer.data
        })
