
from .models import *
from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from datetime import date
from .forms import CartForm
import random, string, functools, json
from django.contrib import messages


# Create your views here.
def index(request):
    data = {'prod': Product.objects.all(),
            'cart_stock': Cart.objects.filter(user=request.user, order=None).count(),
            'cart': Cart.objects.select_related('product_id').filter(user = request.user, order=None)}
    return render(request, 'pages/index.html', data)

def product_d(request, pk):
    view = Product.objects.get(id=pk)
    view.views += 1
    view.save()
    attr = Product_attr.objects.values('attribute', "stock").filter(product_id=pk).distinct()

    data = {'details': Product.objects.get(id=pk),
            'related_prod': Product.objects.all().order_by('-views')[:10],
            'attr': attr,
            'cart_stock': Cart.objects.filter(user=request.user, order=None).count(),
            'cart': Cart.objects.select_related('product_id').filter(user = request.user, order=None),
            'ximages': XImages.objects.filter(main_product=pk),
            }

    if request.method == 'POST' and request.user.is_authenticated:
        user = request.user
        product_id = pk
        product_attr = request.POST.get('attr')
        count = request.POST.get('num-product')
        cart = Cart(None, user, product_id, product_attr, count)

        
        cart.save()
        
    return render(request, 'pages/product-detail.html', data)
    
def product(request):
    data = {'prod': Product.objects.all(),
            'cart_stock': Cart.objects.filter(user=request.user, order=None).count(),
            'cart': Cart.objects.select_related('product_id').filter(user = request.user, order=None)}
    return render(request, 'pages/product.html', data)

def cart_display(request):
    data = {'cart_stock': Cart.objects.filter(user=request.user, order=None).count(),
            'cart': Cart.objects.select_related('product_id').filter(user = request.user, order=None),
            'shipping': Shipping.objects.all()} 
    if request.method == 'POST':
        if request.POST.get('last-name') and request.POST.get('first-name') and request.POST.get('phone') and request.POST.get('address') and request.POST.get('phuong'):
            res = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
            user = request.user
            name = request.POST.get('last-name')+" "+request.POST.get('first-name')
            address = request.POST.get('address')+" "+request.POST.get('phuong')+" "+request.POST.get('district')+" "+"Thành phố Hồ Chí Minh"
            sdt = request.POST.get('phone')
            shipping = Shipping.objects.get(district=request.POST.get('district')).shipping_cost
            method = request.POST.get('method')
            order = Order(None, res, user, name, address, sdt, shipping, date.today(), method)
            
            cart = Cart.objects.filter(user=request.user)
            
            for i in cart:
                if i.order == None:
                    i.order = res
                    i.save()
            if Cart.objects.filter(order=res).count() != 0:
                order.save()
            
    return render(request, 'pages/cart.html', data)

def invoice(request, order):
    data = {'cart_stock': Cart.objects.filter(user=request.user, order=None).count(),
            'cart': Cart.objects.select_related('product_id').filter(order=order),
            'order': Order.objects.get(order_code=order)}
    
    return render(request, 'pages/invoice.html', data)

def check_out(request, user):
    data = {'cart_stock': Cart.objects.filter(user=user, order=None).count(),
            'cart': Cart.objects.select_related('product_id').filter(user=user, order=None),
            'cart2': Cart.objects.select_related('product_id').filter(user=user),
            'order_code': Order.objects.filter(user=user).order_by('-id'),}
    
    return render(request, 'pages/checkout.html', data)

def delete(request):
    id1 = request.GET.get('id')
    Cart.objects.get(id=id1).delete()
    data = {
        'deleted': True,
        'id': id1
    }
    return JsonResponse(data)

def CartData(request):
    cart = Cart.objects.select_related('product_id').filter(user = request.user, order=None)
    cart_stock = Cart.objects.filter(user=request.user, order=None).count(),
   
    # convert tuple into integer  
    stock = int(functools.reduce(lambda sub, ele: sub * 10 + ele, cart_stock))

    # stringify json string data into an array
    id = json.dumps(request.GET.get('id')).replace("[", "").replace("]", "").replace("\\\"", "").replace("\"", "").split(',')
    count = json.dumps(request.GET.get('count')).replace("[", "").replace("]", "").replace("\\\"", "").replace("\"", "").split(',')

    for i in range(1, (stock+1)):
        instance = Cart.objects.get(id = id[i])
        # print(id[i] + ": " + count[i])
        instance.count = count[i]
        instance.save()

    return JsonResponse({'update': 'success'})

def Search(request):
    result = request.GET.get('search')
    data = { 'searched_prod': Product.objects.filter(title__contains = result),
            'cart_stock': Cart.objects.filter(user=request.user, order=None).count(),
            'cart': Cart.objects.select_related('product_id').filter(user = request.user, order=None)}

    return render(request, 'pages/search.html', data)



def Payment(request):
    res = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    while(Cart.objects.filter(order=res).count() == 1):
        res = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    user = request.user
    name = json.dumps(request.GET.get('info'), ensure_ascii=False).encode('utf8').decode().replace("[", "").replace("]", "").replace("\"", "").replace("\\", "")
    address = json.dumps(request.GET.get('address'), ensure_ascii=False).encode('utf8').decode().replace("[", "").replace("]", "").replace("\"", "").replace("\\", "")
    sdt = json.dumps(request.GET.get('phone'), ensure_ascii=False).encode('utf8').decode().replace("[", "").replace("]", "").replace("\"", "").replace("\\", "")
    ship = json.dumps(request.GET.get('ship'), ensure_ascii=False).encode('utf8').decode().replace("[", "").replace("]", "").replace("\"", "").replace("\\", "")
    shipping = str(Shipping.objects.get(district=ship).shipping_cost)
    order = Order(None, res, user, name, address, sdt, shipping, date.today(), "paypal")
    cart = Cart.objects.filter(user=request.user)
            
    for i in cart:
        if i.order == None:
            i.order = res
            i.save()
    if Cart.objects.filter(order=res).count() != 0:
        order.save()
    
    return JsonResponse({'isPaid': True})

# def WishList(request):
#     return HttpResponse("WISH_LIST")



