from django.conf.urls import patterns, include, url

urlpatterns = patterns('api.views',

    url(r'^get_dormitory/$', 'get_dormitory'),

    url(r'^purchase/research', 'get_production_by_research'),
#    url(r'^purchase/time_list/$', 'time_list'),
#    url(r'^purchase/hit_list/$', 'hit_list'),
#    url(r'^purchase/purchase_list$', 'purchase_list$'),


)
