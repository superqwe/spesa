# from pprint import pprint as pp
# from pprint import pprint as pp

from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from spesa import views_util
from spesa.models import Acquisto, Prodotto

from pprint import pprint as pp


# todo: da aggiungere pulsante per cancellare tutti i prodotti acquistati

def index(request, azione=None, pk=None):
    if azione == 'elimina' and pk == 'tutto':
        acquistati = Acquisto.objects.filter(stato='1')

        for acquisto in acquistati:
            acquisto.stato = 0
            acquisto.save()

    else:
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
    da_comprare = [(acquisto, views_util.prezzo(acquisto.prodotto)) for acquisto in da_comprare]

    comprato = Acquisto.objects.filter(stato='1')

    # todo: nel caso di più prezzi per un prodotto, selezionare quello del negozio dove si effettua l'acquisto
    # seleziona il prezzo più basso
    # prezzo = [views_util.prezzo(acquisto.prodotto.nome)[0].prezzo for acquisto in comprato]
    prezzo = []
    for acquisto in comprato:

        try:
            p = views_util.prezzo(acquisto.prodotto)[0].prezzo
            prezzo.append(p)
        except IndexError:
            print('*** %s senza prezzo ***' % acquisto.prodotto)

    prezzo_totale = sum(prezzo)

    n_da_comprare = len(da_comprare)
    n_comprato = len(comprato)
    n_totale = n_da_comprare + n_comprato

    pagina = 'spesa'

    return render(request, 'spesa/spesa.html', locals())


def lista_prodotti_da_aggiungere(request):
    if request.method == 'POST':

        for key, value in request.POST.items():

            if key.startswith('ck'):
                try:
                    acquisto = Acquisto.objects.get(prodotto__id=value)
                    acquisto.stato = '2'
                    acquisto.save()

                except Acquisto.DoesNotExist:
                    prodotto = Prodotto.objects.get(id=value)
                    acquisto = Acquisto.objects.create(prodotto=prodotto, stato='2')
                    acquisto.save()

            elif key.startswith('nuovo-prodotto'):
                prodotto = Prodotto.objects.create(nome=value)
                acquisto = Acquisto.objects.create(prodotto=prodotto, stato='2')
                acquisto.save()

                nuovo_prodotto = prodotto

    prodotti = views_util.lista_prodotti_fuori_carrello()

    pagina = 'aggiungi_prodotti'
    return render(request, 'spesa/aggiungi_prodotto.html', locals())
