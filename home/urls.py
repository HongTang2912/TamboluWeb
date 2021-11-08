from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.index, name = 'home'),
    path('product-detail/<str:pk>', views.product_d, name='product-detail'),
    path('product', views.product, name = 'product'),
    path('cart', views.cart_display, name = 'cart'),
    path('checkout/<str:order>', views.check_out, name = 'checkout')
]