from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Product, Order, Cart

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home:home', 'home:cart', 'home:search']
    
    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    def items(self):
        return Product.objects.all()

class InvoiceSitemap(Sitemap):
    def items(self):
        return Order.objects.all()

class CheckoutSitemap(Sitemap):
    def items(self):
        return Cart.objects.all()