# Generated by Django 3.2.5 on 2021-10-27 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('type_product', models.CharField(choices=[('women', '1'), ('men', '2'), ('bag', '3'), ('shoes', '4'), ('watches', '5')], default='1', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_attr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(default='color', max_length=100)),
                ('data', models.CharField(default='red', max_length=100)),
                ('stock', models.IntegerField(default=0)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('count', models.IntegerField(default=1)),
                ('product_attr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product_attr')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='product_attr',
            constraint=models.UniqueConstraint(fields=('product_id', 'attribute', 'data'), name='unq_prod'),
        ),
    ]
