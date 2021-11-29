from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_image','title', 'price', 'type_product')
admin.site.register(Product, PostAdmin)

class Post_attrAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'attribute', 'stock')
    list_filter = ('product_id',)
admin.site.register(Product_attr, Post_attrAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order', 'product_id', 'product_attr','count')
    list_filter = ('order',)
    search_fields = ['order',]
admin.site.register(Cart, CartAdmin)

class ShipAdmin(admin.ModelAdmin):
    list_display = ('district', 'shipping_cost')
admin.site.register(Shipping, ShipAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_code', 'user', 'name', 'address', 'phone_number', 'shipping_cost', 'date')
admin.site.register(Order,OrderAdmin)

class XAdmin(admin.ModelAdmin):
    list_display = ('main_product', 'extensive_img')
    list_filter = ('main_product', )
    search_fields = [ 'extensive_img',]
admin.site.register(XImages, XAdmin)

