from pprint import pprint as pp

from django.db.models.query_utils import Q
from django.db.utils import ConnectionDoesNotExist

from spesa.models import Prodotto, Prezzo, Carrello


def prezzo(prodotto):
    prezzi = Prezzo.objects.filter(prodotto__id=prodotto.id)

    return prezzi


def lista_prodotti_fuori_carrello():
    q_da_comprate = Q(stato='2')
    q_comprato = Q(stato='1')

    id_acquisti_nel_carrello = Carrello.objects.filter(q_da_comprate | q_comprato).values_list('prodotto',
                                                                                               flat=True)

    fuori_carrello = Prodotto.objects.exclude(pk__in=list(id_acquisti_nel_carrello))

    return fuori_carrello
