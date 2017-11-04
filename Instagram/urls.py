from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .import views

urlpatterns=[
    url(r'^$' , views.index, name = 'index'),
    url(r'^Iniciar_sesion/$', auth_views.LoginView.as_view(template_name = 'Iniciar_sesion.html',redirect_authenticated_user=True),name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(),name='logout'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^profile/$', views.profile, name = 'profile'),
]
