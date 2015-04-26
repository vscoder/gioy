from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #url(r'^$', 'gioy.views.home', name='home'),

    url(r'^$', 'home.views.index', name='home'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^ads/', include('ads.urls', namespace='ads')),
    url(r'^admin/', include(admin.site.urls)),
]
