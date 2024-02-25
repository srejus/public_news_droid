from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *

# Create your views here.

class LoginView(View):
    def get(self,request):
        err = request.GET.get("err")
        return render(request,'login.html',{'err':err})

    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            acc = Account.objects.get(user=request.user)
            if acc.user_type == 'reporter':
                return redirect("/reporter/")
            
            return redirect("/")
        err = "Invalid credentails!"
        return redirect(f"/account/login/?err={err}")
    

class SignupView(View):
    def get(self,request):
        err = request.GET.get("err")
        return render(request,'signup.html',{'err':err})

    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        user_type = request.POST.get("user_type")
        pincode = request.POST.get("pincode")
        gender = request.POST.get("gender")

        if password != password1:
            err = "Password not matching!"
            return redirect(f"/accounts/signup?err={err}")
    
        user = User.objects.filter(username=username)
        if user.exists():
            err = "User with this username already exists"
            return redirect(f"/accounts/signup?err={err}")
        
        acc = Account.objects.filter(Q(email=email) | Q(phone=phone)).exists()
        if acc:
            err = "User with this phone or email already exists"
            return redirect(f"/accounts/signup?err={err}")
        
        user = User.objects.create_user(username=username,email=email,password=password)

        Account.objects.create(user=user,full_name=full_name,email=email,phone=phone,
                               gender=gender,user_type=user_type,pincode=pincode)

        return redirect("/accounts/login")
    

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("/")
    

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self,request):
        try:
            acc = Account.objects.get(user=request.user)
        except Account.DoesNotExist:
            return redirect("/")
        return render(request,'profile.html',{'acc':acc})