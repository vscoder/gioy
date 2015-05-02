from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /ads/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /ads/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /ads/category/
    url(r'^category/$', views.categories, name='categories'),
    # ex: /ads/category/4/
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category_detail, name='category_detail'),
]
