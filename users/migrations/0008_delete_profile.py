# Generated by Django 5.0.3 on 2024-03-30 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
