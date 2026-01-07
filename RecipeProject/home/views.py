from .models import Recipe
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    
    recipes = Recipe.objects.all()
    context = {"recipes" : recipes}
    return render(request, 'home/index.html', context)

@login_required(login_url="/user/login")
def create_page(request):
    
    if request.method == "POST":

        recipe_name = request.POST.get("recipe_name")
        recipe_description = request.POST.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")
        Recipe.objects.create(recipe_name=recipe_name, recipe_description=recipe_description, recipe_image=recipe_image, recipe_owner = request.user)
        return redirect('/')
    
    return render(request, 'home/create.html')

def recipe_page(request, recipe_id):
    
    recipe = Recipe.objects.get(id = recipe_id)
    context = {"recipe" : recipe}
    return render(request, 'home/recipe.html', context)

@login_required(login_url="/user/login")
def update_page(request, recipe_id):
    
    recipe = Recipe.objects.get(id = recipe_id)
    context = {"recipe" : recipe}

    if recipe.recipe_owner != request.user:
        messages.error(request, "Not authorized to update recipe!")
        return redirect('/')

    if request.method == "POST":

        if recipe.recipe_owner == request.user:
            recipe.recipe_name = request.POST.get("recipe_name")
            recipe.recipe_description = request.POST.get("recipe_description")
            recipe.recipe_image = request.FILES.get("recipe_image")
            recipe.save()
            return redirect('/')
        
        else:
            messages.error(request, "Not authorized to update recipe!")
            return redirect('/')

    return render(request, 'home/update.html', context)
