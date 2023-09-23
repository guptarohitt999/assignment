from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import Upload 
# Create your views here.

def logIn(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('upload')
        else:
            message="Username or Password is incorrect!!!"
            context={'message':message}
            return render(request,"login.html",context)

    return render (request,'login.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        print(uname,email,pass1,pass2)
    
        if pass1!=pass2:
            message="Your password and confirm password are not Same!!"
            context={'message':message}
            print(message)
            return render(request,'signup.html',context)
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render(request,'signup.html')
    
@login_required(login_url="login")
def upload(request):
    if request.method=='POST':
        profile=request.FILES['pic']
        fileUpload=request.FILES['file']
        print(profile,fileUpload)
        en=Upload(profile=profile,doc=fileUpload)
        en.save()
        var=Upload.objects.all().values()
        print(var[len(var)-1])
        var1=var[len(var)-1]
        print(var1['profile'])
        return render(request,"upload.html",var1)
        
    return render(request,"upload.html")

def LogoutPage(request):
    return redirect('login')
