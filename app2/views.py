from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def lokesh(request):
    return HttpResponse('Happy Birthday Lokesh')