from django.http import HttpResponse


def test_view(request):
    s = 'test!!!'
    return HttpResponse(s)


def page_view(request):
    s = 'page!!!'
    return HttpResponse(s)
