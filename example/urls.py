from django.conf.urls import patterns, url, include
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^{{ app_name }}/', include('{{ app_name }}.urls')),
    (r'^admin/', include(admin.site.urls)),
)

