from recipes.models import Category

menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add recipe', 'url_name': 'about'},
        {'title': 'Log in', 'url_name': 'about'}
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_cat'] = 0
        return context
