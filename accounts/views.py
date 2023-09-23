import time
import uuid
import re

from django.shortcuts import render , redirect 
from CONFIG import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import profile
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site
from shop.models import Cart 
from CONFIG.urls import *






def home(request):
    cart = []
    lenth =0
    if request.user.is_authenticated:
        lenth = len(Cart.objects.filter(user=request.user))
        cart = Cart.objects.filter(user = request.user)
    return render(request,'home.html',{'cart':cart,'cart_len':lenth})
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email,password=password)
        if user :
            if user.is_superuser == True and user.is_staff==True and user.is_active== True:
                login(request,user)
                messages.success(request,'User Logged in!')
                return redirect('admin')
            elif user.is_staff == True and user.is_active== True:
                login(request,user)
                messages.success(request, "Username Logged in!")
                return redirect('staff')
            elif user.is_active==True:
                login(request,user)
                messages.success(request,'User Logged in!')
                return redirect('home')
            else:
                messages.error(request,'Please Verify Your Account!')
                return redirect('register')
        else:
            messages.error(request,'Cant Find User, Please enter correct username and password.')
    return render(request, 'accounts/login.html')
def logout_user(request):
    logout(request)
    messages.success(request,'User Logged Out, Successfully')
    return redirect('login')
    

def success(request):
     return render(request,'accounts/success.html')

def regerror(request):
     return render(request,'accounts/regerror.html')
def uuid_5min():
    while True:
        new_uuid = uuid.uuid4()
        print("Generated UUID:", new_uuid)
        time.sleep(300)  # Sleep for 5 minutes (300 seconds)

def register(request):
    if request.method == 'POST':
            name = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password1 = request.POST.get('password1')
            if password != password1:
                messages.warning(request, "password must be same")
            elif password == password1:
                #name cheak
                if User.objects.filter(username= name).exists():
                    messages.warning(request, "username already taken")
                    return redirect('register')
                # email cheak
                elif User.objects.filter(email= email).exists():
                    messages.warning(request, "email already taken")
                    return redirect('register')
                
                
                # strong pass cheak
                elif len(password)<8:
                    messages.warning(request, "password must be at least 8 characters long")
                    return redirect('register')
                
                # elif not any(c.isupper() for c in password) or not any(c.islower() for c in password):
                #     messages.warning(request, "password must be contains both uppercase and lowercase letters")
                #     return redirect('regiister')
                # elif not any(c.isdigit() for c in password):
                #     messages.warning(request, "password must be contains at least one digit")
                #     return redirect('register')
                # elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                #     messages.warning(request, "password must be contains at least one special character (e.g., !, @, #, $, etc.)")
                #     return redirect('register')


                # save everyting
                else:
                    try:
                        user = User.objects.create(username=name,email=email,password=password)
                        user.set_password(password)
                        user.save()
                        auth_token = uuid.uuid4()
                        
                        prof_obj = profile(user=user, user_auth_token=auth_token)
                        prof_obj.save()
                        
                        send_verification_email(request,user,auth_token)
                        messages.success(request, "A verification email has been sent to your email address. Activate your account to login")
                        return redirect('login')
                    except Exception as e:
                        print(e)
                        return redirect('regerror')
                         
                    
    return render(request, 'accounts/register.html')


def send_verification_email(request,user,auth_token):
    
    subject = 'Verify Your Tatka Shop Account'
    site = get_current_site(request)
    message = f'Hi {user.username}, please click the link below to verify your Tatka Shop account:\n\n' \
              f'http://{site}/verify/{auth_token}/'
    plain_message = strip_tags(message)
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    send_mail(subject, plain_message, from_email, recipient_list, html_message=message)
    

def verify_account(request, auth_token):
    try:
        profile_obj = profile.objects.get(user_auth_token=auth_token)
        if not profile_obj.is_verified:
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, "Your account has been verified successfully. You can now log in.")
        else:
            messages.info(request, "Your account is already verified. You can log in.")
    except Exception as e:
        messages.error(request, "Invalid verification link.")

    return redirect('login')  

def dashboard(request):
    cart = []
    lenth =0
    if request.user.is_authenticated:
        lenth = len(Cart.objects.filter(user=request.user))
        cart = Cart.objects.filter(user = request.user)
    return render(request,'accounts/cus-dashbord.html',{'cart':cart,'cart_len':lenth})


        

