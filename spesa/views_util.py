from pprint import pprint as pp

from django.db.models.query_utils import Q
from django.db.utils import ConnectionDoesNotExist

from spesa.models import Prodotto, Prezzo, Carrello, Categoria


def prezzo(prodotto):
    prezzi = Prezzo.objects.filter(prodotto__id=prodotto.id)

    return prezzi


def lista_prodotti_fuori_carrello():
    q_da_comprate = Q(stato='1')
    q_comprato = Q(stato='0')

    id_acquisti_nel_carrello = Carrello.objects.filter(q_da_comprate | q_comprato).values_list('prodotto',
                                                                                               flat=True)

    fuori_carrello = Prodotto.objects.exclude(pk__in=list(id_acquisti_nel_carrello))

    return fuori_carrello


def lista_prodotto_per_categoria():
    categorie = Categoria.objects.all()

    prodotti_per_categoria = []
    for categoria in categorie:
        prodotti = Prodotto.objects.filter(categoria=categoria, carrello__stato=None)
        prodotti_per_categoria.append((categoria, prodotti))

    prodotti_vari = Prodotto.objects.filter(categoria=None)

    prodotti_per_categoria.append(('Vari', prodotti_vari))

    return prodotti_per_categoria
