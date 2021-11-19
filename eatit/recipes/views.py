from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


def index(request):
    return render(request, 'recipes/home.html')


def categories(request):
    return HttpResponse("<h1>Categories</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found!!</h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'recipes/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Registration")
        return dict(list(context.items()) + list(c_def.items()))
