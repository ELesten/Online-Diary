# Generated by Django 4.1.1 on 2022-09-22 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='currency',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
