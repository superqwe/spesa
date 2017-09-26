from django.contrib import admin

from .models import Prodotto


class ProdottoAdmin(admin.ModelAdmin):
    list_display = ('da_comprare', 'nome')


admin.site.register(Prodotto, ProdottoAdmin)
