# Generated by Django 3.2.5 on 2021-12-01 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20211201_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='method',
            field=models.CharField(default='regular', max_length=100),
        ),
    ]