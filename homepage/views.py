from django.shortcuts import render

from catalog.models import catalog_item as Item


def home(request):
    items = Item.objects.homepage()

    context = {
        'items': items,
    }

    return render(request, 'homepage/index.html', context)


def login(request):
    template = "homepage\index.html"
    form = forms.Form(request.POST or None)
    context = {
        'form': form
    }

    if request.method == 'POST' and form.is_valid():
        send_mail(
            'Тема письма',
            'Тело письма',
            'from@example.form',
            ['to_1example']
        )

    return render(request, 'homepage/login.html', context)
