# from pprint import pprint as pp
# from pprint import pprint as pp

from django.http import HttpResponse
from django.shortcuts import render

from spesa.models import Acquisto


def index(request, azione=None, pk=None):
    if pk:
        acquisto = Acquisto.objects.get(pk=pk)

        if azione == 'acquistato':
            acquisto.stato = 1

        elif azione == 'elimina':
            acquisto.stato = 0

        elif azione == 'riacquista':
            acquisto.stato = 2

        acquisto.save()

    da_comprare = Acquisto.objects.filter(stato='2')
    comprato = Acquisto.objects.filter(stato='1')
    n_da_comprare = len(da_comprare)
    n_comprato = len(comprato)
    n_totale = n_da_comprare + n_comprato

    return render(request, 'spesa/lista_prodotti.html', locals())
