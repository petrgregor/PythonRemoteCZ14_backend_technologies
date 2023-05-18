from django.shortcuts import render
from django.http import HttpResponse


# regular expression
def hello(request, s):
    return HttpResponse(f'Hello, {s} world!')


# URL encoding
def hello2(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} world!')
