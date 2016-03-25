
from django.conf.urls import patterns, include, url
from django.contrib import admin
import terryspace
from terryspace.blog import views as blog_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'terryspace.views.home', name='home'),
    # url(r'^terryspace/', include('terryspace.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^omret/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$','django.views.static.serve',
        {'document_root':terryspace.settings.STATICFILES_DIRS, 'show_indexes': True}),
    url(r'^$','terryspace.views.home',name='home'),
    

    #url(r'^about/$','resume.views.about'),                   
    url(r'^blog/$',blog_views.blog_list),
    url(r'^eclipseblog/$',blog_views.blog_eclipse),
    url(r'^pythonblog/$',blog_views.blog_python),
    url(r'^javablog/$',blog_views.blog_java),
	url(r'^lifeblog/$',blog_views.blog_life),
)
