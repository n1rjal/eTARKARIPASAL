from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserLoginForm,UserJobForm,GeodataForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as user_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def adduser(request):
    form=UserRegisterForm()
    jform=UserJobForm()
    gform=GeodataForm()
    if request.method=="GET":
        return render(request,"user/signup.html",{"form":form,"jform":jform,"gform":gform})

    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        jform=UserJobForm(request.POST)
        gform=GeodataForm(request.POST)
        if form.is_valid() and jform.is_valid() and gform.is_valid():
            
            username=request.POST.get("username")
            messages.success(request,"Succesfully created user for {}".format(username))
            
            user=form.save(commit=True)
            
            GEO=gform.save(commit=False)
            GEO.user=user

            JOB=jform.save(commit=False)
            JOB.user=user
        
            JOB.save()
            GEO.save()
            return redirect("login")
        
        else:
            messages.error(request,"Invalid Entry")
            return render(request,"user/signup.html",{"form":form,"jform":jform,"gform":gform})


# Create your views here.
def authuser(request):
    form=UserLoginForm()
    if request.method=="GET":
        return render(request,"user/login.html",{"form":form})

    if request.method=="POST":
        form=UserLoginForm(request.POST)
        username=request.POST.get("username")
        password=request.POST.get("password")
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in sucessfully")
            return redirect("homepage")
        else:
            messages.error(request,"Invalid username or password")
            return redirect("login")

def logout(request):
    user_logout(request)
    request.session['cartitems']=[]
    return render(request,"user/logout.html")

@login_required
def profile(request):
    logged_user=request.user
    display=True
    if logged_user.job.job=="TK":
        display=False
    print(logged_user.id)    
    return render(request,"user/profile.html",{"display":display})

@login_required
def update(request):
    
    form=UserRegisterForm(instance=request.user)
    jform=UserJobForm(instance=request.user.job)
    gform=GeodataForm(instance=request.user.geodata)
    if request.method=="GET":
        return render(request,"user/update.html",{"form":form,"jform":jform,"gform":gform})

    if request.method=="POST":
        form=UserRegisterForm(request.POST,instance=request.user)
        jform=UserJobForm(request.POST,instance=request.user.job)
        gform=GeodataForm(data=request.POST,instance=request.user.geodata)

        print(request.POST["password1"])
        if form.is_valid() and jform.is_valid():
            user=form.save(commit=True)
        
            JOB=jform.save(commit=False)
            JOB.user=user

            GEOFORM=gform.save(commit=False)
            GEOFORM.user=user

            JOB.save()
            GEOFORM.save()


            #messages.success
            messages.success(request,"Your profile is updated")
            user=authenticate(username=request.POST['username'],password=request.POST['password1'])
            if user is not None:
                login(request,user)
            return redirect('profile')
        else:
            return render(request,"user/update.html",{"form":form,"jform":jform,"gform":gform})

def searchuser(request,username):
    #lets search user by name
    searchuser=User.objects.filter(username=username).first()
    try:
        if request.user.username!=searchuser.username:
            return render(request,"user/searchuser.html",{"user":searchuser})
        else:
            return redirect('profile')
    except:
        return render(request,"user/searchuser.html",{"user":searchuser})