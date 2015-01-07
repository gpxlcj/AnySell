from django.conf.urls import patterns, include, url

urlpatterns = patterns('api.views',
    url(r'^get_dorm_by_district/$', 'get_dorm_by_district'),
)
