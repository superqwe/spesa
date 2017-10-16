# from pprint import pprint as pp
# from pprint import pprint as pp

from django.http import HttpResponse
from django.shortcuts import render

from spesa import views_util
from spesa.models import Acquisto, Prodotto

from pprint import pprint as pp


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
    da_comprare = [(acquisto, views_util.prezzo(acquisto.prodotto.nome)) for acquisto in da_comprare]

    comprato = Acquisto.objects.filter(stato='1')
    n_da_comprare = len(da_comprare)
    n_comprato = len(comprato)
    n_totale = n_da_comprare + n_comprato

    pagina = 'spesa'

    return render(request, 'spesa/spesa.html', locals())

def lista_prodotti_da_aggiungere(request):
    prodotti = Prodotto.objects.all()
    return render(request, 'spesa/aggiungi_prodotto.html', locals())
