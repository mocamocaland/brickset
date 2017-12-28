from django.conf.urls import url

from . import views


urlpatterns = [
    #url(r'^hello/$', views.hello, name='hello'),
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post'),
    url(r'^news/(?P<slug>[-\w]+)/$', views.news, name='news'),

]