from django.urls import path, include

from rest_framework import routers 

from store.rest_views import UserViewSet, DishViewSet, CategoryViewSet, CustomObtainAuthToken, CartViewSet

# Urls do not need entering slack since base ends in slash
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"dishes", DishViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"carts", CartViewSet)

urlpatterns= [
    path("", include(router.urls)), 
    path("authenticate/", CustomObtainAuthToken.as_view()),
    path("api-login/", include("rest_framework.urls")),
]


