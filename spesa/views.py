from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from .models import Prodotto


# from pprint import pprint as pp


def index(request):
    return HttpResponse("ciao bello")


