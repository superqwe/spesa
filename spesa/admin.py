from django.contrib import admin

from spesa.models import Acquisto, Prodotto


class AcquistoAdmin(admin.ModelAdmin):
    list_display = ('prodotto', 'quantita', 'stato')


class ProdottoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca')


admin.site.register(Acquisto, AcquistoAdmin)
admin.site.register(Prodotto, ProdottoAdmin)
