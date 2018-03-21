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

    # Registration and account creation
    url(r'^profile_registration', views.register_profile, name='register_profile'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^picture/add/$', views.PictureCreate.as_view(), name='picture-add'),

    # For submitting ratings and comments
    url(r'^review/$', views.rate, name='review'),

    # For adding and deleting dive sites to and from favorites
    url(r'^add-my-list/$', views.add_my_list, name='add_my_list'),
    url(r'^remove-my-list/(?P<divesite_id>[\w\-]+)/$', views.remove_from_my_list, name='remove_from_my_list'),

    # Delete user account
    url(r'^delete-account/$', views.delete_account, name='delete_account'),
]