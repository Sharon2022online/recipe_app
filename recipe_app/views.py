from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
from django.contrib import messages
from django.db.models import Max

# Create your views here.



def register(request):
    return render(request,'register.html')

def c_profile(request):
    return render(request,'c_profile.html')

def add_recipe(request):
    return render(request,'add_recipe.html')

# Login

def all_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        j=registration.objects.filter(email=user_name, password=password)
        print(j)
        for i in j:
            print(i.chef)
        ul = registration.objects.filter(email=user_name, password=password,chef=True)
        print(ul)
        uc=registration.objects.filter(email=user_name,password=password,chef=False)
        print(f"uc count: {len(uc)}")
        if len(ul) == 1:
            print("chef")
            for i in j:
                id=i.id
                request.session['id']=id
                b=registration.objects.filter(id=id)
                return render(request,'c_profile.html',{"b":b})
        elif len(uc) == 1:
            print("User")
            return redirect("/")
        else:
            messages.info(request,"Invalid credentials")
            print("invalid")

            return render(request,"login.html")

        
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, 'login.html',context)

# Registration
    
def add(request):
    print(request.POST)
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        chef=request.POST.get('chef', False) == 'YES'
        password=request.POST['password']
        if request.method == 'POST' and request.FILES['pic']:
            pic = request.FILES['pic']
        else:
            pic = None

        if registration.objects.filter(email=email):
            messages.info(request,"Email Already Exist")
            return render(request,'register.html')
        elif registration.objects.filter(name=name):
            messages.info(request,"Username Already Exist")
            return render(request,'register.html')
        else:
            reg=registration(name=name,email=email,chef=chef,password=password,pic=pic)
            reg.save()
            return render(request,'login.html')
    else:
        return render(request,'register.html')


def c_profile(request):
    user_id = request.session.get('id')
    user = registration.objects.get(id=user_id)
    context = {'user': user}
    return render(request, 'c_profile.html', context)

# Display all Chef list
def index(request):
    chefs = registration.objects.filter(chef=True)
    print(len(chefs))
    context = {'chefs': chefs}
    return render(request,'index.html', context)

