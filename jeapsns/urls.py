from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from jeapsns.views import index, hello, zwn, current_time, index_temp, index_temp_c, index_temp_file

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jeapsns.views.home', name='home'),
    # url(r'^jeapsns/', include('jeapsns.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^hello/$', hello),
    (r'^zwn/$', zwn),
    (r'^time/(get)/(\d{1,2}/$)', current_time),
    (r'^index_temp/([a-zA-Z0-9]{1,10})/([a-f0-9]{1,6})$', index_temp_c),
    (r'^index_temp_file/([a-f0-9]{1,6})$', index_temp_file),
    (r'^index_temp/([a-zA-Z0-9]{1,10})$', index_temp),
    
    (r'^.*$', index), 
)
