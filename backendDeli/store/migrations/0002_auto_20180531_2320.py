# Generated by Django 2.0.5 on 2018-06-01 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='total_ingredients',
        ),
        migrations.AddField(
            model_name='dish',
            name='description',
            field=models.CharField(default='good food', max_length=200),
        ),
    ]