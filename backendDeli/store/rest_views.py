from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.authentication import  TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import list_route


from apis.serializers import UserSerializer, DishSerializer, CategorySerializer
from .models import Dish, Category


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Adding authentication and permission class to restrict access


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    # authentication_classes = ( TokenAuthentication, SessionAuthentication )
    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     query = self.request.GET.get("q")
    #     if query:
    #         q_set = Dish.objects.filter(dish_name__icontains=query)
    #     else:
    #         q_set = Dish.objects.all()
    #     return q_set


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    authentication_classes = ( TokenAuthentication, SessionAuthentication )
    permission_classes = (IsAuthenticated,)


# # Creating custom user method to get token.  Can be done different ways
# # http://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
# class CustomObtainAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
#         token = Token.objects.get(key=response.data["token"])
#         user = User.objects.get(id=token.user_id)
#         serializer = UserSerializer(user, many= False)
#         return Response({
#             "token": token.key, "user": serializer.data
#         })
