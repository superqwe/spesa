from django.db.utils import ConnectionDoesNotExist

from spesa.models import Prodotto, Prezzo


def prezzo(nome_prodotto):
    print('\n',nome_prodotto)
    # try:
    prezzi = Prezzo.objects.filter(prodotto__nome=nome_prodotto)
    # except:
    #     print('*')
    #     prezzi = None

    return prezzi
