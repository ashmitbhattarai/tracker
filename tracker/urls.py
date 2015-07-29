from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^stdpages/', include('stdpage.urls')),
    (r'^makeuser/', include('usermod.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'tracker.views.login'),
    url(r'^accounts/auth/$', 'tracker.views.auth_view'),
    url(r'^accounts/logout/$', 'tracker.views.logout'),
    url(r'^accounts/loggedin/$', 'tracker.views.loggedin'),
    url(r'^accounts/invalid/$', 'tracker.views.invalid_login'),
    url(r'^home/$', 'tracker.views.home'),
    url(r'^files1upload/$','tracker.views.files_upload'),
    url(r'^files/$', 'tracker.views.files'),
    url(r'^download/(?P<upoad1_id>\d+)/$', 'tracker.views.download'),
    url(r'^contacts/$', 'tracker.views.contact'),
    url(r'^search/$', 'tracker.views.search_users'),
    url(r'^dashboard/$', 'tracker.views.dashboard'),
    url(r'^timeline/$', 'tracker.views.timeline'),
    url(r'^fileupload', 'tracker.views.fileupload'),
    url(r'^filebrowser', 'tracker.views.filebrowser')

)
