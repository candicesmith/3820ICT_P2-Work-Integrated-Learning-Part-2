# Generated by Django 3.2 on 2021-09-14 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0016_auto_20210914_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user_id',
        ),
    ]
