from django.views.generic import TemplateView

from catalog.models import catalog_item as Item


class Home(TemplateView):
    model = Item
    template_name = 'homepage/index.html'

    def get_queryset(self):
        return Item.objects.homepage()
