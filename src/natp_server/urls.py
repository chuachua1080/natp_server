from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
admin.autodiscover()
import views, authorize, search, kml

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'natp_server.views.home', name='home'),
    # url(r'^natp_server/', include('natp_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$',authorize.login),
    url(r'^accounts/logout/$', authorize.logout),
    url(r'^$',views.index),
    url(r'^natp_server/$', views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_probe/$',views.add_probe),
    url(r'^show_probe/$',views.show_probe),
    url(r'^show_ident/$',views.show_ident),
    url(r'^show_position/$',views.show_position),

    url(r'^show_vector/$', views.show_vector),
    url(r'^save_db/$', views.update_from_file),
    url(r'^report/$', views.update_from_report),
    url(r'^kml/$', kml.output_kml),
  
    url(r'^search_probe/$',search.search_probe),
    url(r'^search_position/$',search.search_position),
    url(r'^search_vector/$',search.search_vector),
    url(r'^search_ident/$',search.search_ident),

)