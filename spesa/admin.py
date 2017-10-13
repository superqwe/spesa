from django.contrib import admin

from spesa.models import Acquisto, Prodotto, Negozio, Prezzo


class AcquistoAdmin(admin.ModelAdmin):
    list_display = ('prodotto', 'quantita', 'stato')


class ProdottoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca')


class PrezzoAdmin(admin.ModelAdmin):
    list_display = ('prodotto', 'negozio', 'prezzo', 'prezzo_in_offerta')


admin.site.register(Acquisto, AcquistoAdmin)
admin.site.register(Negozio)
admin.site.register(Prodotto, ProdottoAdmin)
admin.site.register(Prezzo, PrezzoAdmin)
