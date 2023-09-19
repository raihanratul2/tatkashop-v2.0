from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login_user,name='login'),
    path('logout/',views.logout_user, name='logout') ,
    path('register/',views.register,name='register'),
    path('success/',views.success,name='success'),
    path('regerror/',views.regerror,name='regerror'),
    path('verify/<str:auth_token>/',views.verify_account,name='verify'),
    path('dashboard/',views.dashboard,name='dashboard'),
    
    # path('pass_reset_req/', views.password_reset_request, name='password_reset_request'),
    # path('reset-pass/',views.resetpass,name='reset_pass'),
    # path('login/',views.login_acc,name='login_acc')
]
