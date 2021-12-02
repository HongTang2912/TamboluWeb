from django.urls import path
from home.sitemaps import *
from django.contrib.sitemaps.views import sitemap
from . import views

sitemaps = {
    'static': StaticViewSitemap,
    'product': ProductSitemap,
    'invoice': InvoiceSitemap,
    'checkout': CheckoutSitemap
}

app_name = 'home'
urlpatterns = [
    path('', views.index, name = 'home'),
    path('product-detail/<str:pk>', views.product_d, name='product-detail'),
    path('product', views.product, name = 'product'),
    path('cart', views.cart_display, name = 'cart'),
    path('invoice/<str:order>', views.invoice, name = 'invoice'),
    path('checkout/<str:user>', views.check_out, name = 'checkout'),
    path('delete', views.delete, name = 'delete'),
    path('cart-data', views.CartData, name = 'cart-data'),
    path('search', views.Search, name = 'search'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('payment', views.Payment, name = 'payment'),
    # path('wishlist', views.WishList, name = 'wishlist'),
]