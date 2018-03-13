from django.conf.urls import url, include
from scotDives import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.index, name='index'),
    url(r'^dive-map/', views.divemap, name='divemap'),
    url(r'^dive-sites/', views.divesites, name='divesites'),
    url(r'^dive-site/(?P<divesite_name_slug>[\w\-]+)/$', views.show_site, name='show_site'),
    url(r'^club-map/', views.clubmap, name='clubmap'),
    url(r'^photo-gallery/', views.photogallery, name='photogallery'),
    url(r'^search/', views.search, name='search'),
    url(r'^contact-us/', views.contact, name='contact'),
    url(r'^sitemap/', views.sitemap, name='sitemap'),

    #--imam--
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
]