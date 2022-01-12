from recipes.models import Category

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add recipe', 'url_name': 'about'},
        {'title': 'Calories plan', 'url_name': 'about'},
        {'title': 'Water plan', 'url_name': 'about'},
        {'title': 'Log in', 'url_name': 'about'},
        {'title': 'Sign up', 'url_name': 'about'},
        ]


class DataMixin:
    paginate_by = 10

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_cat'] = 0
        return context
