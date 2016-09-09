
from django.conf.urls import url
from . import views

app_name = 'viewone'
urlpatterns = [
    #ex: /viewone/
    url(r'^$', views.index, name='index'),
    #ex: /viewone/Imris Inc./company/
    #url(r'^test/', views.test, name='test'),
    url(r'^(?P<co_name>[\w()/&\-,. ]+)/company/$', views.company, name='company'),
    url(r'^(?P<award_id>[0-9]+)/nsfawards/$', views.nsfawards, name='nsfawards'),
    url(r'^displayall/', views.displayall, name='displayall'),
    url(r'^searchcompany/', views.searchcompany, name='searchcompany'),
    url(r'^searchpubmed/', views.searchpubmed, name='searchpubmed'),
    url(r'^home/', views.home, name='home'),
    url(r'^searchnsfawards/',views.searchnsfawards, name='searchnsfawards'),
    #url(r'^(?P<co_name>[\w\-,. ]+)/comdetails/$', views.comdetails, name='comdetails'),

]
