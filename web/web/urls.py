#! -*-coding:utf8-*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
import apps.account.urls
import apps.api.urls
admin.autodiscover()

#管理页面
urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
)


#主页面
urlpatterns += patterns('apps.home.views',

    url(r'^$', 'index'),
    url(r'^index/$', 'index'),
    url(r'^search/$', 'index'),
    url(r'^product/?P<pro>[0-9]+/', 'product_info'),
    url(r'^production_list/$', 'production_list'),
)

#用户系统
urlpatterns += patterns('',

    url(r'^account/', include(apps.account.urls)),
    url(r'^api/', include(apps.api.urls)),
)

