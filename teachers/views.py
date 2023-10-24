from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to eMobilis")


def about(request):
    return HttpResponse("About eMobilis")


def contact(request):
    return HttpResponse("This is the Contact page")
