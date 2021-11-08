
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import CartForm
# Create your views here.
def index(request):
    data = {'prod': Product.objects.all(),
            'cart_stock': Cart.objects.filter(user=request.user, order=None).count(),
            'cart': Cart.objects.filter(user = request.user, order=None)}
    return render(request, 'pages/index.html', data)

def product_d(request, pk):
    attr = Product_attr.objects.values('attribute').filter(product_id=pk).distinct()
    data = {'details': Product.objects.get(id=pk),
            'attr': attr,
            'stock': Product_attr.objects.values('attribute', 'stock').filter(product_id=pk).distinct(),
            'cart_stock': Cart.objects.filter(user=request.user, order=None).count(),
            'cart': Cart.objects.filter(user = request.user, order=None)}
    
    if request.method == 'POST':
        user = request.POST.get('user')
        p_image = request.POST.get('product_image')
        product_id =  Product.objects.get(title=request.POST.get('title')).id
        price = request.POST.get('price')
        product_attr =  request.POST.get('product_attr')
        count = request.POST.get('stock')
        cart = Cart(None, user, p_image, product_id, price, product_attr, count)
        cart.save()
        
    return render(request, 'pages/product-detail.html', data)
def product(request):
    data = {'prod': Product.objects.all(),
            'cart_stock': Cart.objects.filter(user=request.user, order=None).count(),
            'cart': Cart.objects.filter(user = request.user, order=None)}
    return render(request, 'pages/product.html', data)

def cart_display(request):
    data = {'cart_stock': Cart.objects.filter(user=request.user, order=None).count(),
            'cart': Cart.objects.filter(user = request.user, order=None),
            'shipping': Shipping.objects.all()} 
    if request.method == 'POST':
        if request.POST.get('result'):
            res = request.POST.get('result')
            Cart.objects.get(id=res).delete()
        elif request.POST.get('last-name') and request.POST.get('first-name') and request.POST.get('phone') and request.POST.get('address') and request.POST.get('phuong'):
            res = request.POST.get('MDH')
            name = request.POST.get('last-name')+" "+request.POST.get('first-name')
            address = request.POST.get('address')+" "+request.POST.get('phuong')+" "+request.POST.get('district')+" "+"Thành phố Hồ Chí Minh"
            sdt = request.POST.get('phone')
            print(name)
            print(address)
            print(sdt)
            order = Order(None, res, name, address, sdt)
            cart = Cart.objects.filter(user=request.user)
            
            for i in cart:
                if i.order == None:
                    i.order = res
                    i.save()
            if Cart.objects.filter(order=res).count() != 0:
                order.save()
            
    return render(request, 'pages/cart.html', data)

def check_out(request, order):
    data = {'cart_stock': Cart.objects.filter(user=request.user, order=None).count(),
            'cart': Cart.objects.filter(user = request.user, order=order),
            'order': Order.objects.get(order_code=order)}
    
    return render(request, 'pages/checkout.html', data)





