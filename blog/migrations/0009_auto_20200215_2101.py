# Generated by Django 3.0.2 on 2020-02-15 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200215_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_date',
            new_name='created_date',
        ),
    ]
