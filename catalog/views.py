from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, FormView, ListView

from catalog.models import catalog_item as Item
from rating.forms import AddMarkForm
from rating.models import Mark


class Item_list(ListView):
    model = Item
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.catalog().order_by('name', 'category')


class Item_detail(DetailView, FormView):
    model = Item
    """Возможно выглядит, как колхоз, зато работает"""

    def get(self, request, pk):
        item = get_object_or_404(Item.objects.catalog(), pk=pk)
        marks = Mark.objects.filter(item_id=pk)
        count_marks = len(marks)
        try:
            average_mark = sum([user.mark for user in marks]) / count_marks
        except ZeroDivisionError:
            average_mark = 0

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
        return render(request, 'catalog/item_detail.html', context)

    def post(self, request, pk):
        item = get_object_or_404(Item.objects.catalog(), pk=pk)
        marks = Mark.objects.filter(item_id=pk)
        count_marks = len(marks)
        try:
            average_mark = sum([user.mark for user in marks]) / count_marks
        except ZeroDivisionError:
            average_mark = 0

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
