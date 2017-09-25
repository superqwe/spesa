from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from .models import Prodotto


# from pprint import pprint as pp


def index(request):
    return HttpResponse("ciao bello")


def lista_da_comprare(request):
    out = Prodotto.objects.order_by('nome').filter(da_comprare=True)
    out_json = serializers.serialize('json', out)
    out_json = {"dati": out_json}

    return JsonResponse(out_json)


def lista_comprati(request):
    out = Prodotto.objects.order_by('nome').filter(da_comprare=False)
    out_json = serializers.serialize('json', out)
    out_json = {"dati": out_json}

    return JsonResponse(out_json)


def liste(request):
    da_comprare = Prodotto.objects.order_by('nome').filter(da_comprare=True)
    comprato = Prodotto.objects.order_by('nome').filter(da_comprare=False)

    context = {'da_comprare': da_comprare,
               'comprato': comprato}

    return render(request, 'spesa/lista_prodotti.html', context)
