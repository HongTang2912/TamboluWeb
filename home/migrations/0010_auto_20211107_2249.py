# Generated by Django 3.2.5 on 2021-11-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
