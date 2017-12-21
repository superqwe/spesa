from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    visualizza_nota = models.BooleanField(default=False)
    note = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"

    def __str__(self):
        return '%s' % self.nome


class Prodotto(models.Model):
    class Meta:
        ordering = ('nome', 'marca')
        verbose_name = "Prodotto"
        verbose_name_plural = "Prodotti"

    def __str__(self):
        marca = self.marca if self.marca else ''
        categoria = self.categoria if self.categoria else ''
        return '%s - %s - %s' % (self.nome, marca, categoria)

    nome = models.CharField(max_length=100)
    marca = models.CharField(null=True, blank=True, max_length=50)
    categoria = models.ForeignKey(Categoria, null=True, blank=True)


class Carrello(models.Model):
    DA_COMPRARE = 1
    COMPRATO = 0
    STATO_PRODOTTO = (
        (DA_COMPRARE, 'Da comprare'),
        (COMPRATO, 'Comprato'),
    )

    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    quantita = models.IntegerField(default=1)
    stato = models.IntegerField(choices=STATO_PRODOTTO, default=1)

    class Meta:
        ordering = ('prodotto',)
        verbose_name = "Carrello"
        verbose_name_plural = "Carrello"

    def __str__(self):
        return '%s - %s' % (self.prodotto, self.quantita)


class Negozio(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = "Negozio"
        verbose_name_plural = "Negozi"

    def __str__(self):
        return '%s' % self.nome


class Prezzo(models.Model):
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    negozio = models.ForeignKey(Negozio, on_delete=models.CASCADE)
    prezzo = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    prezzo_in_offerta = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('prodotto', 'prezzo', 'negozio')
        verbose_name = "Prezzo"
        verbose_name_plural = "Prezzi"

    def __str__(self):
        return '%s - %s - %s' % (self.prodotto, self.negozio, self.prezzo)
