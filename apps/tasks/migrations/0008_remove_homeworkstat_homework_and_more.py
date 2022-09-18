# Generated by Django 4.1.1 on 2022-09-12 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_remove_homeworkstat_status_homeworkstat_homework_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeworkstat',
            name='homework',
        ),
        migrations.AddField(
            model_name='homework',
            name='homework_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='homework', to='tasks.homeworkstat'),
        ),
    ]