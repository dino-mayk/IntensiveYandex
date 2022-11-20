from django.shortcuts import get_object_or_404, render

from catalog.models import catalog_item as Item


def item_list(request):
    items = Item.objects.catalog().order_by('name', 'category')

    context = {
        'items': items,
    }

    return render(request, 'catalog/item_list.html', context)


def item_detail(request, pk):
    item = get_object_or_404(Item.objects.catalog(), pk=pk)

    context = {
        'item': item,
    }

    return render(request, 'catalog/item_detail.html', context)
