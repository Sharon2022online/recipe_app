from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
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
            return redirect("login")
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


# View Recipes Of The Specific User

def edit_recipe(request):
    chef = registration.objects.get(email=request.session.get('user_name'))
    recipes = Recipe.objects.filter(publish=chef)
    
    return render(request, 'edit_recipe.html', {'recipes': recipes})
           
def view_recipe(request):
    r_id = request.GET.get('id')
    r =  Recipe.objects.filter(publish=int(r_id))
    context = {
            'recipe': r
    }
    return render(request, 'view_recipe.html', context)

# Edit Profile
import os
@login_required
def edit_profile(request):
    chef = registration.objects.get(email=request.session.get('user_name'))
    if request.method == 'POST':
        chef.name = request.POST['name']
        chef.email = request.POST['email']
    
        if len(request.FILES) != 0:
            if len(chef.pic) > 0:
                os.remove(chef.pic.path)
            chef.pic = request.FILES['pic']

        chef.save()
        chef = registration.objects.get(email=request.session.get('user_name'))
        context = {
            'ch': chef
        }
        messages.success(request, 'Updation Successfully')
        return render(request, 'edit_profile.html',context)


    else:
        c_id = request.GET.get('id')
        c = registration.objects.get(id=int(c_id))
        context = {
            'ch': c
        }
        return render(request, 'edit_profile.html', context)
    
# Delete Recipe

def delete_recipe(request):
    if request.method == 'POST':
        recipe_id = request.POST.get('recipe_id')
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            recipe.delete()
            messages.success(request, '!! Deletion Is Successful !!')
        except Recipe.DoesNotExist:
            messages.error(request, ' !!Recipe Does Not Exist !!')
    return redirect('edit_recipe')


def update_recipe(request):
    # Retrieve the recipe from the database using its ID
   
    if request.method == 'POST':
        # If the form has been submitted, update the recipe with the new details

        id = request.POST.get('recipe_id')
        recipe = Recipe.objects.get(id=int(id))

        recipe.recipe_name = request.POST['recipe_name']
        if "description" in request.POST:
            recipe.description = request.POST['description']
        recipe.ingredient = request.POST['ingredient']
        recipe.prep_time = request.POST['prep_time']
        recipe.serves = request.POST['serves']
        recipe.type = request.POST['type']
        if len(request.FILES) != 0:
            if len(recipe.pic) > 0:
                os.remove(recipe.pic.path)
            recipe.pic = request.FILES['pic']
        recipe.save()
        # Redirect the user back to the recipe details page
        
        u=f"http://127.0.0.1:8000/update_recipe?id={id}"
        messages.info(request,"Updated Succesfully")
        return redirect(u)

    # If the form has not been submitted, display the form with the current recipe details
    else:
        id = request.GET.get('id')
        rp = Recipe.objects.get(id=int(id))
        
        context = {
            'r': rp
        }
        return render(request, 'update_recipe.html', context)
    

# Display Veg Recipe
def veg(request):
    veg = Recipe.objects.filter(type='Veg')
    context = {
        'veg': veg
    }
    return render(request, 'veg.html', context)


# Display Non-Veg Recipe
def nonveg(request):
    nonv = Recipe.objects.filter(type='Non-Veg')
    context = {
        'non': nonv
    }
    return render(request, 'nonveg.html', context)


# Recipe Details
def recipe_details(request):
    recipe_id = request.GET['id']
    details = Recipe.objects.get(id=recipe_id)
    context = {'recipe': details}
    return render(request, 'recipe_details.html', context)
