from django.conf.urls import url
from . import views



urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^view/(?P<slug>[^\.]+)/$', views.view_post, name='view_post'),
url(r'^category/(?P<slug>[\w-]+)/$', views.view_category, name='view_category'),
url(r'^/dir/(?P<pk>\d+)/$', views.view_dir, name='view_dir'),
url(r'^like/(?P<slug>[\w-]+)/$', views.like_post, name='like_post'),

]
