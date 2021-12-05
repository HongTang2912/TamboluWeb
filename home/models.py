from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

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
    views = models.IntegerField(null=False, default = 0)
    body = models.TextField(blank=True)
    description = models.TextField(blank=True)
    addition_info = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)
    def get_absolute_url(self):
        return f'/product-detail/{self.id}/'
    
    
class Product_attr(models.Model):
    product_id = models.ForeignKey(Product, null=False,  on_delete=models.CASCADE)
    attribute = models.CharField(null=False, default = 'red', max_length=100)
    stock = models.IntegerField(null=False, default = 1, validators=[MinValueValidator(1)])

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product_id', 'attribute'], name='unq_prod')
        ]
    def __str__(self):
        return self.attribute
    

class Cart(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user = models.CharField(null = False, max_length=100)
    product_id = models.ForeignKey(Product, null=False,  on_delete=models.CASCADE)
    product_attr = models.TextField(max_length=500, null=True)
    count = models.IntegerField(default=1, null= False, validators=[MinValueValidator(1)])
    order = models.CharField(null = True, max_length=8)

    def get_absolute_url(self):
        return f'/checkout/{self.user}/'

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
    user = models.CharField(max_length=150, null=False)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=1000, null=False)
    phone_number = models.CharField(max_length=14, null = False)
    shipping_cost = models.CharField(max_length=100, null=False)
    date = models.DateField(default=date.today())
    method = models.CharField(max_length=100, null=False, default="regular")
    total = models.CharField(max_length=100, null=False, default="0")
    def __str__(self):
        return self.order_code
    def get_absolute_url(self):
        return f'/invoice/{self.order_code}/'

class XImages(models.Model):
    main_product = models.ForeignKey(Product, null=False,  on_delete=models.CASCADE)
    extensive_img = models.CharField(null=False, unique=True, max_length=100)

