#!-*- coding:utf8 -*-
__author__ = 'gpxlcj'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.account.views',

    url(r'^login/$', 'custom_login'),
    url(r'^logout/$', 'custom_logout'),
    url(r'^register/$', 'custom_register'),
    url(r'^usercenter/$', 'custom_user_center'),
)
