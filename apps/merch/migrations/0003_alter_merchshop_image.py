# Generated by Django 4.1.1 on 2022-09-24 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch', '0002_alter_merchshop_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchshop',
            name='image',
            field=models.ImageField(upload_to='merch.images'),
        ),
    ]
