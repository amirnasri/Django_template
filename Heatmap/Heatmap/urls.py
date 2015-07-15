from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from HelloWorldApp.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Heatmap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index1/(?P<idx>[0-9]+)', index, name = 'index'),
)
