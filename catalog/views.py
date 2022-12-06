from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from catalog.models import catalog_item as Item
from rating.models import Mark

from .forms import AddMarkForm


def item_list(request):
    items = Item.objects.catalog().order_by('name', 'category')

    context = {
        'items': items,
    }

    return render(request, 'catalog/item_list.html', context)


def item_detail(request, pk):
    item = get_object_or_404(Item.objects.catalog(), pk=pk)
    try:
        init_mark = Mark.objects.get(Q(user_id=request.user.id)
                                 & Q(item_id=pk)).mark
    except Mark.DoesNotExist:
        init_mark = ''
    print(init_mark)
    form = AddMarkForm(request.POST or None,
                       initial={Mark.mark.field.name: init_mark}
                       )
    context = {
        'item': item,
        'form': form
    }

    if request.method == "POST" and form.is_valid():
        mark = form.cleaned_data.get('mark')
        Mark.objects.update_or_create(user_id=request.user.id,
                                      item_id=pk,
                                      defaults={'mark': mark})

        print(mark)

    return render(request, 'catalog/item_detail.html', context)
