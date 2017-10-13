# from pprint import pprint as pp
# from pprint import pprint as pp

from django.http import HttpResponse
from django.shortcuts import render

from spesa.models import Acquisto


def index(request):
    da_comprare = Acquisto.objects.filter(stato = '2')
    comprato = Acquisto.objects.filter(stato = '1')

    return render(request, 'spesa/lista_prodotti.html', locals())
