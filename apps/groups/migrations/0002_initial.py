# Generated by Django 4.1.1 on 2022-09-25 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'role': 'Teacher'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lead_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
