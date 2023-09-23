from django.urls import path
from . import views
urlpatterns = [
    path('',views.products,name='products'),
    path('Category/',views.category, name='Category'),
    path('product/<str:slug>/',views.product_view,name='product_view'),
    path('cart/<int:id>',views.cart,name='cart'),
]
