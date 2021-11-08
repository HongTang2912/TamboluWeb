# Generated by Django 3.2.5 on 2021-11-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='shipping_cost',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]