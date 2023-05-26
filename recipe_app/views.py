from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.db.models import Avg

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
            request.session['uid'] = ul[0].id
            return render(request,'c_profile.html', {'b': b})
        elif len(uc) == 1:
            print("User")
            request.session['user_name'] = uc[0].email
            request.session['uid'] = uc[0].id
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
    if request.method == "POST":
        first_name = request.POST.get("f_name")
        email = request.POST["email"]
        chef = request.POST.get('chef')
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'register.html')
        
        if request.method == 'POST' and request.FILES['pic']:
            pic = request.FILES['pic']
        else:
            pic = None

        if registration.objects.filter(email=email):
            messages.error(request, "Email already exists")
            return render(request, 'register.html')
        elif registration.objects.filter(name=first_name):
            messages.error(request, "Username already exists")
            return render(request, 'register.html')
        else:
            reg = registration(name=first_name, email=email, chef=chef, password=password, pic=pic)
            reg.save()
            messages.success(request, "Registration successful")
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
    r =  Recipe.objects.filter(publish=int(r_id)).annotate(avg_rating=Avg('rating__rating'))
    context = {
            'recipe': r
    }
    return render(request, 'view_recipe.html', context)

# Edit Profile
import os

def edit_profile(request):
    chef = registration.objects.get(id=request.session.get('uid'))
    if request.method == 'POST':
        chef.name = request.POST['name']
        chef.email = request.POST['email']
    
        if len(request.FILES) != 0:
            if len(chef.pic) > 0:
                os.remove(chef.pic.path)
            chef.pic = request.FILES['pic']

        chef.save()
        chef = registration.objects.get(id=request.session.get('uid'))
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

#Update Recipe
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
    veg = Recipe.objects.filter(type='Veg').annotate(avg_rating=Avg('rating__rating'))
    context = {
        'veg': veg
    }
    return render(request, 'veg.html', context)


# Display Non-Veg Recipe
def nonveg(request):
    nonv = Recipe.objects.filter(type='Non-Veg').annotate(avg_rating=Avg('rating__rating'))
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

# User Profile
def user_profile(request):
    user = registration.objects.get(email=request.session['user_name'])
    context = {'user': user}
    return render(request, 'user_profile.html', context)


# Save Recipe
def save_recipe(request):
    recipe_id = request.GET['id']
    user_id = request.session['user_name']
    recipe = Recipe.objects.get(id=recipe_id)
    user = registration.objects.get(email=user_id)

    # Check if the recipe is already saved by the user
    if SavedRecipe.objects.filter(user=user, recipe=recipe).exists():
        messages.info(request, "This recipe is already saved.")
    else:
        saved_recipe = SavedRecipe(user=user, recipe=recipe)
        saved_recipe.save()
        messages.info(request, "Recipe saved successfully.")
    f=f"http://127.0.0.1:8000/recipe_details?id={recipe_id}"
    return redirect(f)

# All Recipe Rating
def all(request):
    recipes = Recipe.objects.all().annotate(avg_rating=Avg('rating__rating'))
    context = {'recipes': recipes}
    return render(request, 'all_recipes.html', context)

# Rating
def add_rating(request):
    if request.method == 'POST':
        recipe_id = request.GET.get('id')
        user_id = request.session['user_name']
        rating=request.POST.get('rating')
        recipe = Recipe.objects.get(id=recipe_id)
        user = registration.objects.get(email=user_id)
        saved_recipe =Rating(user=user, recipe=recipe,rating=rating)
        saved_recipe.save()
        recipe_id = request.GET['id']
        details = Recipe.objects.get(id=recipe_id)
        context = {'recipe': details}
        messages.info(request,"Rating Submitted") 
        return render(request, 'recipe_details.html', context)

        
        # return redirect(recipe_details)
    # return redirect(recipe_details)
    else:
        return render(request, 'recipe_details.html', context)

def favourites(request):
    user_id = request.session['user_name']
    user = registration.objects.get(email=user_id)
    fav = SavedRecipe.objects.filter(user=user)
    for i in fav:
        name=i.recipe
        print(name)
    
    context = {'fa': fav}
    # context = {'fa': fav}
    return render(request, 'favourites.html', context)


