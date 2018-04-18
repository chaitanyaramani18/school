

# Create your views here.
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
         )


from .forms import UserLogInForm, UserRegisterForm


# Create your views here.




def index(request):
    return render(request,"index.html")

def loginview(request):
    title = 'login'
    form = UserLogInForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect("/")


        # user =authenticatenticate(username)

    return render(request,"login.html",{"form":form,'title':title})

def logoutview(request):
    return render(request,"accounts.html")

def registerview(request):
    title = 'RegistrationForm'
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return redirect("/")



    return render(request,"accounts.html",{"form":form,'title':title})

