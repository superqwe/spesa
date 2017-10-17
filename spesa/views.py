# from pprint import pprint as pp
# from pprint import pprint as pp

from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

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

    # todo: nel caso di più prezzi per un prodotto, selezionare quello del negozio dove si effettua l'acquisto
    # seleziona il prezzo più basso
    # prezzo = [views_util.prezzo(acquisto.prodotto.nome)[0].prezzo for acquisto in comprato]
    prezzo = []
    for acquisto in comprato:

        try:
            p = views_util.prezzo(acquisto.prodotto.nome)[0].prezzo
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

        for pk in request.POST.values():

            try:
                acquisto = Acquisto.objects.get(prodotto__id=pk)
                acquisto.stato = '2'
                acquisto.save()

            except Acquisto.DoesNotExist:
                prodotto = Prodotto.objects.get(id=pk)
                acquisto = Acquisto.objects.create(prodotto=prodotto, stato='2')
                acquisto.save()

            except ValueError:
                print(pk)

    prodotti = views_util.lista_prodotti_fuori_carrello()

    pagina = 'aggiungi_prodotti'
    return render(request, 'spesa/aggiungi_prodotto.html', locals())
