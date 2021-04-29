from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import *

from .forms import Add_recipe, Add_Image


# Create your views here.
class Homepage(ListView):
    model = Recipie_Model
    template_name = 'main/home.html'
    paginate_by = 9
    context_object_name = 'recipes'

    # Передача контеста в шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class Recipe_detail_view(DetailView):
    model = Recipie_Model
    template_name = 'main/detail.html'
    context_object_name = 'recipe'


class Update_rec_view(UpdateView):
    model = Recipie_Model
    template_name = 'main/add_recipe.html'
    form_class = Add_recipe
    success_url = '/'



class Delete_rec_view(DeleteView):
    model = Recipie_Model
    success_url = '/'
    template_name = 'main/delete_rec.html'


class Add_recipe_view_class(CreateView):
    model = Recipie_Model
    template_name = 'main/add_recipe.html'
    form_class = Add_recipe
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'titile'
        return context


def search(request):
    return render(request, 'main/r_search.html')


def Search_ing(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        search_results = Recipie_Model.objects.filter(ingred__contains=searched.lower())
        return render(request, 'main/search_res.html', {'searched': searched,
                                                        'search_results': search_results})
    else:
        return render(request, 'main/search_res.html', {})


def Search_all(request):
    if request.method == 'POST':
        searched = request.POST['searched_all']
        search_results = Recipie_Model.objects.filter(title__contains=searched.capitalize())
        return render(request, 'main/search_res.html', {'searched': searched,
                                                        'search_results': search_results})
    else:
        return render(request, 'main/search_res.html', {})
