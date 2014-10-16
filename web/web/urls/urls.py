from django.conf.urls import patterns, include, url

#from django.contrib import admin
import xadmin
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'xadmin/',include(xadmin.site.urls)),
    
    #url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns = patterns('',
#    url(r'^api/', include('apps.api.url'))
#    url(r'')

#)
