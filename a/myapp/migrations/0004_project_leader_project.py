# Generated by Django 4.2.6 on 2023-11-27 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_task_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Leader_project',
            field=models.CharField(blank=True, default='En proceso de eleccion', max_length=60),
        ),
    ]