#! -*-coding:utf8-*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
import apps.account.urls
admin.autodiscover()

#管理页面
urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
)


#主页面
urlpatterns += patterns('apps.home.views',

    url(r'^$', 'index'),
    url(r'^index/$', 'index'),
    url(r'^/search/$', 'index'),
)

#用户系统
urlpatterns += patterns('',
    url(r'^account/', include(apps.account.urls)),
)

