# Generated by Django 3.2.7 on 2021-09-16 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_auto_20210916_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='uploads/default.png', upload_to='uploads/'),
        ),
    ]
