from django.conf.urls import patterns, url, include
from views import SimpleModelList, SimpleModelDetail

from models import SimpleModel

urlpatterns = patterns('',
    url(r'^$', SimpleModelList.as_view(), name="simplemodel_list"),
    url(r'^(?P<slug>[\w-]+)/', SimpleModelDetail.as_view(), name="simplemodel_detail")
)