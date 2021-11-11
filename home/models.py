from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class Product(models.Model):
    product_image = models.CharField(null=False, unique=True, max_length=100)
    title = models.CharField(max_length=100, null=False, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, null= False)
    category_type = [
        ('women', '1'),
        ('men','2'),
        ('bag', '3'),
        ('shoes', '4'),
        ('watches', '5'),
    ]
    type_product = models.CharField(default = '1',
        max_length=50,
        choices= category_type,
        null=True
    )

    def __str__(self):
        return str(self.id)
    
class Product_attr(models.Model):
    product_id = models.ForeignKey(Product, null=False,  on_delete=models.CASCADE)
    attribute = models.CharField(null=False, default = 'red', max_length=100)
    stock = models.IntegerField(null=False, default = 0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product_id', 'attribute'], name='unq_prod')
        ]
    def __str__(self):
        return self.attribute
    

class Cart(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.CharField(null = False, max_length=100)
    product_image = models.CharField(null = False, max_length=100)
    product_id = models.ForeignKey(Product, null=False,  on_delete=models.CASCADE)
    product_slug = models.CharField(null=True, max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0, default = 0, null = False)
    product_attr = models.TextField(max_length=500, null=True)
    count = models.IntegerField(default=1, null= False)
    order = models.CharField(null = True, max_length=8)

class Shipping(models.Model):
    dis_choices = [
        ('Quận 1', '1'),
        ('Quận 2','2'),
        ('Quận 3', '3'),
        ('Quận 4','4'),
        ('Quận 5', '5'),
        ('Quận 6','6'),
        ('Quận 7', '7'),
        ('Quận 8','8'),
        ('Quận 9', '9'),
        ('Quận 10','10'),
        ('Quận 11', '11'),
        ('Quận 12','12'),
        ('Quận Bình Tân', '13'),
        ('Quận Bình Thạnh','14'),
        ('Quận Gò Vấp', '15'),
        ('Quận Phú Nhuận','16'),
        ('Quận Tân Bình', '17'),
        ('Quận Tân Phú','18'),
        ('Thành Phố Thủ Đức', '19'),
        ('Huyện Bình Chánh','20'),
        ('Huyện Cần Giờ', '21'),
        ('Huyện Củ Chi','22'),
        ('Huyện Hóc Môn', '23'),
        ('Huyện Nhà Bè','24'),
    ]
    district = models.CharField(default = '1',
        max_length=50,
        choices= dis_choices,
        primary_key=True
    )
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=0, default = 0, null = False)

class Order(models.Model):
    order_code = models.CharField(null = False, max_length=8, unique=True)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=1000, null=False)
    phone_number = models.DecimalField(max_digits=14, decimal_places=0, null = False)
    shipping_cost = models.CharField(max_length=100, null=False)
    date = models.DateField(default=date.today())

    def __str__(self):
        return self.order_code
