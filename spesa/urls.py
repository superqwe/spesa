from django.conf.urls import url

from spesa import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^spesa/$', views.index, name='index'),
]
