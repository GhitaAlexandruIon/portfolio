# Generated by Django 3.0.3 on 2020-03-27 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20200324_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(height_field=True, null=True, upload_to='blog/img', width_field=True),
        ),
    ]
