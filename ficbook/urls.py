from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from users import urls as users_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ficbook.views.home', name='home'),
    url(r'^', include(users_urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
