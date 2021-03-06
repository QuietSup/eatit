import operator
from functools import reduce

from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.db.models import Count

from recipes.forms import *
from recipes.models import *
from recipes.utils import DataMixin, menu


# def index(request):
#     recipes = Recipe.objects.all()
#     cats = Category.objects.all()
#     return render(request, 'recipes/index.html', {'title': 'eatit', 'recipes': recipes, 'cats': cats})


class Home(ListView):
    paginate_by = 10
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context


def show_post(request, post_id):
    recipe = Recipe.objects.filter(id=post_id).first()
    return render(request, 'recipes/recipe.html', {'recipe': recipe})


def categories(request):
    return HttpResponse("<h1>Categories</h1>")


def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                # form.save()
                new_post = form.save(commit=False)
                new_post.author = request.user
                new_post.save()
                form.save_m2m()
                return redirect('')
            except:
                form.add_error(None, 'Error')
    else:
        form = AddRecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})


class MyRecipes(DataMixin, ListView):
    model = Recipe
    template_name = 'recipes/my_recipes.html'
    context_object_name = 'recipes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context

    def get_queryset(self):
        # cate = self.request.GET.getlist("cat")
        # queryset = Recipe.objects.filter(cat__in=cate).annotate(num_tags=Count('cat')).filter(num_tags=len(cate))
        # queryset = Recipe.objects.filter(reduce(operator.and_, [Q(cat__in=c) for c in cate]))
        # queryset = Recipe.objects.filter(cat__in=self.request.GET.getlist("cat"))
        if self.request.user.is_authenticated:
            queryset = Recipe.objects.filter(author_id=self.request.user)
        else:
            queryset = []
        return queryset


def del_recipe(request, post_id):

    Recipe.objects.filter(id=post_id).delete()
    cats = Category.objects.all()
    recipes = Recipe.objects.all()
    return render(request, 'recipes/my_recipes.html', {'recipes': recipes, 'cats': cats})


def update_article(request, post_id):
    instance = Recipe.objects.get(id=post_id)
    if request.method == 'POST':
        form = UpdateRecipeForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UpdateRecipeForm(instance=instance)
    return render(request, 'recipes/add_recipe.html', {'form': form})


def favorites(request):
    return HttpResponse("<h1>favorites</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found!!</h1>')


# def login(request):
#     return render(request, 'recipes/login1.html', {'title': 'Log in'})
#

def show_category(request, cat_id):
    return HttpResponse(f'Show category with id = {cat_id}')


class FilterRecipes(DataMixin, ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context

    def get_queryset(self):
        cate = self.request.GET.getlist("cat")
        queryset = Recipe.objects.filter(cat__in=cate).annotate(num_tags=Count('cat')).filter(num_tags=len(cate))
        # queryset = Recipe.objects.filter(reduce(operator.and_, [Q(cat__in=c) for c in cate]))
        # queryset = Recipe.objects.filter(cat__in=self.request.GET.getlist("cat"))
        return queryset.distinct()


class Search(DataMixin, ListView):
    """Search by a recipe name"""
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        context["cats"] = Category.objects.all()
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    # form_class = RegisterUserForm
    template_name = 'recipes/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Registration")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'recipes/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Log in")
        return dict(list(context.items()) + list(c_def.items()))

    # def get_success_url(self):
    #     return reverse_lazy('')


def logout_user(request):
    logout(request)
    return redirect('login')
