# Generated by Django 4.0.3 on 2022-03-13 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_path',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
