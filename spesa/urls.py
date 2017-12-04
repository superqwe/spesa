from django.conf.urls import url

from spesa import views

urlpatterns = [
    url(r'(?P<azione>^acquistato|^elimina|^riacquista)/(?P<pk>[0-9]+|tutto)$', views.index, name='index'),
    url(r'^listaprodotti$', views.lista_prodotti_da_aggiungere, name='lista_prodotti_da_aggiungere'),
    url(r'^$', views.index, name='index'),
]
