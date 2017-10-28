from django.conf.urls import url

from .import views

urlpatterns=[
    url(r'^$' , views.index, name = 'index'),
    url(r'^Iniciar_sesion/$', views.login, name = 'Iniciar_sesion'),
]
