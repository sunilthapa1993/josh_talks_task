# Generated by Django 4.2.9 on 2025-03-24 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
