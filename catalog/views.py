from django.shortcuts import render


def item_list(request):
    return render(
        request,
        template_name='catalog/index.html',
        context={}
    )


def item_detail(request, pk):
    # return HttpResponse('число: {}'.format(pk))
    return render(
        request,
        template_name='catalog/index.html',
        context={}
    )
