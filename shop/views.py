from django.shortcuts import render ,redirect
from .models import Category,Product,Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def products(request):
    cart = []
    lenth =0
    if request.user.is_authenticated:
        lenth = len(Cart.objects.filter(user=request.user))
        cart = Cart.objects.filter(user = request.user)
    all_products = Product.objects.all()
    category = Category.objects.all()
    print(category)
    return render(request,'shop/products.html',{'product': all_products,'cart':cart,'cart_len':lenth})


def category(request,slug):
    category = Category.objects.all()
    Cat_product = Category.objects.get(slug = slug) 
    print(Cat_product)
    return redirect(request.META['HTTP_REFERER'],{'category':category})


def product_view(request,slug):
    cart = []
    lenth =0
    if request.user.is_authenticated:
        lenth = len(Cart.objects.filter(user=request.user))
        cart = Cart.objects.filter(user = request.user)
    product = Product.objects.get(slug =slug)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        print(quantity)
    return render(request,'shop/product_view.html',{'product':product,'cart':cart,'cart_len':lenth})


# def cart(request,id):
#     user = request.user
#     product = Product.objects.get(id=id)
#     cart_prod = Cart.objects.filter(user=user, product=product)
#     if product in cart_prod:
#         cart_prod.quantity +=1
#         cart_prod.save()
#     else:
#         cart_prod = Cart.objects.create(user=user,product=product)
#         cart_prod.save()
#     return redirect(request.META['HTTP_REFERER'])


def cart(request, id):
    if request.method == 'POST':
        user = request.user
        product = Product.objects.get(id=id)
        cart_prod, created = Cart.objects.get_or_create(user=user, product=product)
        messages.success(request, "Product added to cart!")
        if not created:
            cart_prod.quantity += 1
            cart_prod.save()
            messages.success(request, "Product added to cart!")

    return redirect(request.META['HTTP_REFERER'])

