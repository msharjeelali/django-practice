from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('create/', views.create_page, name="create_page"),
    path('recipe/<recipe_id>/', views.recipe_page, name="recipe_page"),
    path('update/<recipe_id>', views.update_page, name="update_page")
]