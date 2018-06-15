# Generated by Django 2.0.5 on 2018-06-09 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, related_name='items', to='store.Dish'),
        ),
    ]
