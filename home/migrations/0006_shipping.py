# Generated by Django 3.2.5 on 2021-11-03 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211030_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('district', models.CharField(choices=[('Quận 1', '1'), ('Quận 2', '2'), ('Quận 3', '4'), ('Quận 4', '4'), ('Quận 5', '5'), ('Quận 6', '6'), ('Quận 7', '7'), ('Quận 8', '8'), ('Quận 9', '9'), ('Quận 10', '10'), ('Quận 11', '11'), ('Quận 12', '12'), ('Quận Bình Tân', '13'), ('Quận Bình Thạnh', '14'), ('Quận Gò Vấp', '15'), ('Quận Phú Nhuận', '16'), ('Quận Tân Bình', '17'), ('Quận Tân Phú', '18'), ('Thành Phố Thủ Đức', '19'), ('Huyện Bình Chánh', '20'), ('Huyện Cần Giờ', '21'), ('Huyện Củ Chi', '22'), ('Huyện Hóc Môn', '23'), ('Huyện Nhà Bè', '24')], default='1', max_length=50, primary_key=True, serialize=False)),
                ('shipping_cost', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
