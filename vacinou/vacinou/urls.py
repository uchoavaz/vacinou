from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^/', include('apps.core.urls', name = 'core')),
    url(r'^admin/', include(admin.site.urls)),
)
