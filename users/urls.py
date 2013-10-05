from django.conf.urls import patterns, url
from django.views.generic.simple import direct_to_template
from views import FunficsView, CategoryView, GenreView


urlpatterns = patterns('',
    url(r'^login/$', direct_to_template, {'template': 'login.html'}, "login"),
    url(r'^funfics/$', FunficsView.as_view(), name='funfics'),
    url(r'^categories/(?P<pk>\d+)/', CategoryView.as_view(), name='category'),
    url(r'^genre/(?P<pk>\d+)/', GenreView.as_view(), name='genre'),
    url(r'^$', direct_to_template, {'template': 'home.html'}, "home"),
)
