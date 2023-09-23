from .models import Cart
from django.contrib.auth.decorators import login_required
from accounts.models import User

# @login_required
# def cart_all(request):
#     cart_len = 0
#     if User.is_authenticated:
#         cart_len = len(Cart.objects.filter(user=request.user))
#     return{'lenth': cart_len}