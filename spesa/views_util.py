from pprint import pprint as pp

from django.db.models.query_utils import Q
from django.db.utils import ConnectionDoesNotExist

from spesa.models import Prodotto, Prezzo, Acquisto


def prezzo(nome_prodotto):
    prezzi = Prezzo.objects.filter(prodotto__nome=nome_prodotto)

    return prezzi


def lista_prodotti_fuori_carrello():
    q_da_comprate = Q(stato='2')
    q_comprato = Q(stato='1')

    acquisti_nel_carrello = Acquisto.objects.filter(q_da_comprate | q_comprato)
    prodotti_nel_carrello = set([acquisto.prodotto for acquisto in acquisti_nel_carrello])

    lprodotti = set(Prodotto.objects.exclude(nome='Acquisto__prodotto__nome'))

    return lprodotti - prodotti_nel_carrello
