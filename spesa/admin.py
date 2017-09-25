from django.contrib import admin

from .models import Prodotto


class ProdottoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'da_comprare')


admin.site.register(Prodotto, ProdottoAdmin)
