from django.shortcuts import render,redirect
from .forms import NewUserForm,UserLoginForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def registerView(request):
    if request.method=="POST":
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"Registration Successfull....You can now login!")
            return redirect('login')
    else:
        form=NewUserForm()
    return render(request,'register.html',{"register_form":form})

def loginView(request):
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.error(request,"Username or Password is not valid")
    else:
        form=UserLoginForm()
    return render(request,'login.html',{"login_form":form})

@login_required
def dashboardView(request):
    if request.user.is_authenticated:
        username=request.user.username
        return render(request,'dashboard.html',{"username":username})
    
@login_required
def logoutView(request):
    logout(request)
    return redirect('login')