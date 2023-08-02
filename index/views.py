from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse("Hello World")


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['number'] = [1, 2, 3, 4, 5]
    return render(request, 'runoob.html', context)


