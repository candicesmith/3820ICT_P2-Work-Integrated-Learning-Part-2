# Generated by Django 3.2 on 2021-09-14 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_client_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='client',
            new_name='client_id',
        ),
    ]
