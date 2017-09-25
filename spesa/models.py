from django.db import models

class Prodotto(models.Model):
    nome =  models.CharField(max_length=200)
    da_comprare = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' % (self.nome, self.da_comprare)
