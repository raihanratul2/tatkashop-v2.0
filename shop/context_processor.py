from .models import Cart ,Category
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate 
from django.contrib.auth.models import AnonymousUser 
from accounts.models import User


def Category_all(request):
    return {'category': Category.objects.all()}

# @login_required
# def cart_all(request):
#     cart = Cart.objects.filter(user = request.user)
#     return{'cart': cart}

# def cart_all(request):
#     cart = []
#     item = []
#     lenth =1
#     user = authenticate(user=request.user)
#     try:
#         if user.request.is_authenticated:
#             lenth = 5#len(Cart.objects.filter(user=request.user))
#             item = Cart.objects.filter(user=request.user)[:2]
            
#         elif request.user.is_anonymous:
#             #cart = Cart.objects.get(user=request.user,)
#             cart = [5]
#             lenth = 96
#             print(cart,lenth,item)
#     except:

#         pass
        
#     return{'cart':cart,'item':item,'lenth':lenth}






