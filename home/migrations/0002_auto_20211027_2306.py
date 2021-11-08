# Generated by Django 3.2.5 on 2021-10-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='cart',
            name='product_image',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]