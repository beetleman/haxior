from django.conf.urls import patterns, include, url
from django.contrib import admin
from proxy.views import proxy

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'haxior.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^(?P<url>.*)$', proxy),
                       )
