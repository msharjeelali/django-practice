from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    recipe_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=100, unique=True)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="photos/")
    recipe_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe_name

admin.site.register(Recipe)