# Generated by Django 5.1.2 on 2025-01-07 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_receipe_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipe',
            old_name='User',
            new_name='user',
        ),
    ]
