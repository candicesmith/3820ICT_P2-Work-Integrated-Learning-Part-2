# Generated by Django 3.2 on 2021-07-29 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0014_auto_20210729_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(default='Nothing', upload_to='videos/<property object at 0x000001D52ACF4A40>'),
        ),
    ]