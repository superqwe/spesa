from django.db import models


class Prodotto(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Prodotto"
        verbose_name_plural = "Prodotti"

    def __str__(self):
        return '%s - %s' % (self.nome, self.marca)


class Acquisto(models.Model):
    DA_COMPRARE = 2
    COMPRATO = 1
    FUORI_LISTA = 0
    STATO_PRODOTTO = (
        (DA_COMPRARE, 'Da comprare'),
        (COMPRATO, 'Comprato'),
        (FUORI_LISTA, 'Fuori lista')
    )

    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    quantita = models.IntegerField()
    stato = models.IntegerField(choices=STATO_PRODOTTO, default=0)

    class Meta:
        verbose_name = "Acquisto"
        verbose_name_plural = "Acquisti"

    def __str__(self):
        return '%s - %s - %s' % (self.prodotto, self.quantita, self.stato)
