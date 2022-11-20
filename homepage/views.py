from django.shortcuts import render

from catalog.models import catalog_item as Item


def home(request):
    items = Item.objects.homepage()

    context = {
        'items': items,
    }

    return render(request, 'homepage/index.html', context)
