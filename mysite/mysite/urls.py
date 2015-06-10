from django.conf.urls import patterns, include, url
from django.contrib import admin
from trips.views import hello_world
from trips.views import login
from trips.views import*

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$',login),
	url(r'^hello/$', hello_world),
	url(r'^register/$',register),
	url(r'^data/$',data),
	url(r'^superdata/$',superdata),
	url(r'^modify/$',modify),
	url(r'^sadd/$',sadd),
	url(r'^sdel/$',sdel),
)
