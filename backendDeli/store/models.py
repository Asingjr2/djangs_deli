from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

from base.models import BaseModel

SPICE_LEVEL = (
    ("BLAND", "BLAND"),
    ("MILD", "MILD"),
    ("HOT", "HOT"),
    ("INFERNO", "INFERNO" ),
)

class Dish(BaseModel):
    dish_name = models.CharField(max_length= 200)
    description = models.CharField(max_length= 200, default="good food")
    spice = models.CharField(max_length=10, choices= SPICE_LEVEL, default = "BLAND")
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "dishes"

    def __str__(self):
        return "Dish is {}".format(self.dish_name)


class Category(models.Model):
    slug = models.SlugField(primary_key=True, unique= True)
    dish = models.ManyToManyField(Dish, blank=True)

    class Meta:
            verbose_name_plural = "categories"

    def __str__(self):
        return self.slug
