# Generated by Django 3.2.7 on 2021-09-16 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0003_auto_20210916_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
    ]
