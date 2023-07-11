from django.shortcuts import render
from django.http import HttpResponse


def projectlist(request):
    return HttpResponse("to-do: send a list of projects")