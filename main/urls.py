from .views import *
from django.urls import path

urlpatterns = [
    path('', Homepage.as_view(), name='Home'),
    path('add/', Add_recipe_view_class.as_view(), name='Add-recipe'),
    path('show/<slug>', Recipe_detail_view.as_view(), name='Show'),
    path('show/<slug>/update', Update_rec_view.as_view(), name='Update'),
    path('show/<slug>/delete', Delete_rec_view.as_view(), name='Delete'),
    path('search/', search, name='Rec_search'),
    path('search/search-ing/', Search_ing, name='Search-ing'),
    path('search/search-all/', Search_all, name='Search-all'),
]
