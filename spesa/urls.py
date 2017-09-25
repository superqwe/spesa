from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^s', views.index, name='index'),
    url(r'^lista_da_comprare', views.lista_da_comprare, name='lista_da_comprare'),
    url(r'^lista_comprati', views.lista_comprati, name='lista_comprati'),
    url(r'^liste', views.liste, name='liste'),
]
