from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'gioy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('django.contrib.auth.urls'),
    url(r'^ads/', include('ads.urls', namespace='ads')),
    url(r'^admin/', include(admin.site.urls)),
]
