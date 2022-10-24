from django.http import HttpResponse


def item_list(request):
    return HttpResponse('Список элементов')


def item_detail(reguest, pk):
    return HttpResponse('Цисло: {}'.format(pk))
