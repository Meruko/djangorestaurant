from django.urls import path
from . import views

urlpatterns = [
    path("", views.DishListView.as_view(), name='index_dish'),
    path("<int:pk>/update", views.DishUpdateView.as_view(), name='update_dish'),
    path("<int:pk>/delete", views.delete, name='delete_dish'),
    path("add/", views.add, name='add_dish'),
    path("ingridients/", views.IngridientListView.as_view(), name='index_ingridient'),
    path("ingridients/<int:pk>/update", views.IngridientUpdateView.as_view(), name='update_ingridient'),
    path("ingridients/<int:pk>/delete", views.deleteIngridient, name='delete_ingridient'),
    path("ingridients/add/", views.addIngridient, name='add_ingridient'),
    path("dish_ingridients", views.DishIngridientsListView.as_view(), name='index_dish_ingridients'),
    path("dish_ingridients/<int:pk>/update", views.addComposition, name='update_dish_ingridients'),
]