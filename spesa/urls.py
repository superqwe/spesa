from django.conf.urls import url

from spesa import views

urlpatterns = [
    url(r'(?P<azione>^acquistato|^eliminato|^riacquista)/(?P<pk>[0-9]+)$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
]
