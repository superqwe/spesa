from django.contrib import admin

from spesa.models import Acquisto, Prodotto, Negozio, Prezzo, Categoria


# actions
def fai_da_comprare(modeladmin, request, queryset):
    queryset.update(stato=2)


fai_da_comprare.short_description = 'Segna i selezionati come da comprare'


# opzioni

class AcquistoAdmin(admin.ModelAdmin):
    actions = [fai_da_comprare]
    list_display = ('prodotto', 'quantita', 'stato')
    list_filter = ('stato',)
    search_fields = ['prodotto__nome', 'prodotto__marca']


class ProdottoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca')
    search_fields = ['nome', 'marca']


class PrezzoAdmin(admin.ModelAdmin):
    list_display = ('prodotto', 'negozio', 'prezzo', 'prezzo_in_offerta')
    search_fields = ['prodotto__nome', 'prodotto__marca']


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'note')


admin.site.register(Acquisto, AcquistoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Negozio)
admin.site.register(Prodotto, ProdottoAdmin)
admin.site.register(Prezzo, PrezzoAdmin)
