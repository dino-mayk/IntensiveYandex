from django.http import HttpResponse


def item_list(request):
    return HttpResponse('Список элементов')


def item_detail(reguest, pk):
    if pk == 0:
        return HttpResponse(status=404)

    return HttpResponse('Цисло: {}'.format(pk))
