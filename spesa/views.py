from django.http import HttpResponse
from django.shortcuts import render

from .models import Prodotto


# from pprint import pprint as pp


def index(request):
    return HttpResponse("ciao bello")


def lista_da_comprare(request):
    out = Prodotto.objects.order_by('nome').filter(da_comprare=True)
    titolo = 'da Comprare'
    context = {'prodotti': out, 'titolo': titolo}

    return render(request, 'spesa/lista_prodotti.html', context)


def lista_comprati(request):
    out = Prodotto.objects.order_by('nome').filter(da_comprare=False)
    titolo = 'Comprati'
    context = {'prodotti': out, 'titolo': titolo}

    return render(request, 'spesa/lista_prodotti.html', context)
