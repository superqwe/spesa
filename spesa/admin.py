from django.contrib import admin

from spesa.models import Acquisto, Prodotto, Negozio, Prezzo

# actions
def fai_da_comprare(modeladmin, request, queryset):
    queryset.update(stato=2)
fai_da_comprare.short_description= 'Segna i selezionati come da comprare'

# opzioni

class AcquistoAdmin(admin.ModelAdmin):
    list_display = ('prodotto', 'quantita', 'stato')
    actions = [fai_da_comprare]


class ProdottoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca')


class PrezzoAdmin(admin.ModelAdmin):
    list_display = ('prodotto', 'negozio', 'prezzo', 'prezzo_in_offerta')


admin.site.register(Acquisto, AcquistoAdmin)
admin.site.register(Negozio)
admin.site.register(Prodotto, ProdottoAdmin)
admin.site.register(Prezzo, PrezzoAdmin)
