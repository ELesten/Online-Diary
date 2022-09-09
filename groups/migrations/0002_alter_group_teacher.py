# Generated by Django 4.1.1 on 2022-09-09 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'role': 'users.UserRole.TEACHER'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lead_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
