# app/urls.py

from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^second/$', views.second, name='second'),
    url(r'^puri/$', views.puri, name='puri_ko_samajh_kyun_nahi_ata___meri_jaan_kyun_khati_hai'),
]
