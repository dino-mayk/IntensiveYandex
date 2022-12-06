from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect

from catalog.models import catalog_item as Item
from rating.forms import AddMarkForm
from rating.models import Mark


def item_list(request):
    items = Item.objects.catalog().order_by('name', 'category')

    context = {
        'items': items,
    }

    return render(request, 'catalog/item_list.html', context)


def item_detail(request, pk):
    item = get_object_or_404(Item.objects.catalog(), pk=pk)
    marks = Mark.objects.filter(item_id=pk)
    count_marks = len(marks)
    average_mark = sum([user.mark for user in marks]) / count_marks

    context = {
        'item': item,
        'count_marks': count_marks,
        'average_mark': average_mark
    }

    if request.user.is_authenticated:
        try:
            init_mark = Mark.objects.get(
                Q(user_id=request.user.id) & Q(item_id=pk)
            ).mark
        except Mark.DoesNotExist:
            init_mark = ''
        form = AddMarkForm(
            request.POST or None,
            initial={Mark.mark.field.name: init_mark}
        )
        context['form'] = form

    if request.method == "POST" and form.is_valid():
        mark = form.cleaned_data.get('mark')
        Mark.objects.update_or_create(
            user_id=request.user.id,
            item_id=pk,
            defaults={'mark': mark}
        )

        return redirect('users:user_detail', pk=request.user.id)

    return render(request, 'catalog/item_detail.html', context)
