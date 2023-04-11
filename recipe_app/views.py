from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
from django.contrib import messages
from django.db.models import Max

# Create your views here.
def c_profile(request):
    return render(request,'c_profile.html')

def base(request):
    return render(request,'base.html')

def user_home(request):
    chefs = registration.objects.filter(chef='YES')
    print(len(chefs))
    context = {'chefs': chefs}
    return render(request,'user_home.html',context)

# Display all Chef list
def index(request):
    chefs = registration.objects.filter(chef='YES')
    print(len(chefs))
    context = {'chefs': chefs}
    return render(request,'index.html', context)

# Display Recipes of a Specific Chef
def chef_recipes(request, chef_id):
    chef = registration.objects.get(id=chef_id)
    recipes = Recipe.objects.filter(chef=chef)
    context = {'recipes': recipes}
    return render(request, 'chef_recipes.html', context)

# Login
def all_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        j = registration.objects.filter(email=user_name, password=password)
        print(j)
        for i in j:
            print(i.chef)
        ul = registration.objects.filter(email=user_name, password=password, chef='YES')
        print(ul)
        uc = registration.objects.filter(email=user_name, password=password, chef='NO')
        print(f"uc count: {len(uc)}")
        if len(ul) == 1:
            print("chef")
            for i in j:
                id = i.id
            b=registration.objects.filter(id=id)
            request.session['user_name'] = ul[0].email
            return render(request,'c_profile.html', {'b': b})
        elif len(uc) == 1:
            print("User")
            request.session['user_name'] = uc[0].email
            return redirect('user_home')
        else:
            messages.info(request,"Invalid credentials")
            print("invalid")
            return render(request,"login.html")
    else:
        msg = ''
        context = {'msg1': msg}
        return render(request, 'login.html',context)

# Registration
def add(request):
    print(request.POST)
    if request.method == "POST":
        first_name = request.POST.get("f_name")
        email = request.POST["email"]
        chef = request.POST.get('chef')
        password = request.POST['password']
        if request.method == 'POST' and request.FILES['pic']:
            pic = request.FILES['pic']
        else:
            pic = None

        if registration.objects.filter(email=email):
            messages.info(request, "Email Already Exist")
            return render(request, 'register.html')
        elif registration.objects.filter(name=first_name):
            messages.info(request, "Username Already Exist")
            return render(request, 'register.html')
        else:
            reg = registration(name=first_name, email=email, chef=chef, password=password, pic=pic)
            reg.save()
            return render(request, 'login.html')
    else:
        return render(request, 'register.html')

# Chef Profile
def c_profile(request):
    user_id = request.session.get('id')
    user = registration.objects.get(id=user_id)
    context = {'user': user}
    return render(request, 'c_profile.html', context)

# Add Recipes
def add_recipe(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        prep_time = request.POST.get('prep_time')
        serves = request.POST.get('serves')
        type = request.POST['type']
        r_desc = request.POST.get('r_desc')
        ingredient = request.POST.get('ingredient')
        if request.method == 'POST' and request.FILES['recipe_image']:
            recipe_image = request.FILES['recipe_image']
        else:
            recipe_image = None
        chef_name = request.session['user_name']
        c = registration.objects.get(email=chef_name)
        recipe = Recipe.objects.create(
            recipe_name=recipe_name,
            prep_time=prep_time,
            serves=serves,
            description=r_desc,
            ingredient=ingredient,
            recipe_image=recipe_image,
            type=type,
            publish = c
        )
        recipe.save()
        
        messages.success(request, 'Recipe Published Successfully')
        return redirect('add_recipe')
    
    context = {}
    return render(request, 'add_recipe.html', context)



def edit_recipe(request):
    recipes = Recipe.objects.all()
    return render(request,'edit_recipe.html', {'recipes': recipes})
           
def view_recipe(request):
    return render(request,'view_recipe.html')