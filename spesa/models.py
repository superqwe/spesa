from django.db import models


class Prodotto(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        verbose_name = "Prodotto"
        verbose_name_plural = "Prodotti"

    def __str__(self):
        marca = self.marca if self.marca else ''
        return '%s - %s' % (self.nome, marca)


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
        return '%s - %s' % (self.prodotto, self.quantita)


class Negozio(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Negozio"
        verbose_name_plural = "Negozi"

    def __str__(self):
        return '%s' % self.nome


class Prezzo(models.Model):
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    prezzo = models.DecimalField(max_digits=3, decimal_places=2)
    prezzo_in_offerta = models.DecimalField(null=True, blank=True, max_digits=3, decimal_places=2)
    negozio = models.ForeignKey(Negozio, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Prezzo"
        verbose_name_plural = "Prezzi"

    def __str__(self):
        return '%s - %s - %s' % (self.prodotto, self.negozio, self.prezzo)
