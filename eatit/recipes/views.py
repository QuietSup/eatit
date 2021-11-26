from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from recipes.forms import RegisterUserForm
from recipes.utils import DataMixin


def index(request):
    return render(request, 'recipes/home.html')


def categories(request):
    return HttpResponse("<h1>Categories</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found!!</h1>')


def login(request):
    return HttpResponse("Log in")


def show_post(request, post_id):
    return HttpResponse(f'Show recipe with id = {post_id}')


def show_category(request, cat_id):
    return HttpResponse(f'Show category with id = {cat_id}')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'recipes/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Registration")
        return dict(list(context.items()) + list(c_def.items()))
