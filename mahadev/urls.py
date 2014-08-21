from django.conf.urls import patterns, url

from mahadev import views

urlpatterns = patterns('',
    url(r'^episodes/(?P<ep_id>\d{16})/$',views.playSeries, name='playSeries'),
    url(r'^episodes/(?P<ep_id>\d{16})/(?P<seq>\d{1})/$',views.playSeq, name='playSeq'),
    url(r'^$',views.episodeList, name='episodeList'),
    url(r'^episode/create/$', views.saveEpisode, name='saveEpisode'),
    url(r'^create/$', views.createEpisode, name='createsEpisode'),
    url(r'^episodes/$', views.seriesListView ,name='seriesListView'),

    



)