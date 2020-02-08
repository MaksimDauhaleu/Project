from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login, name='login'),
    url(r'^success$', views.success, name='success'),
    url(r'^user_login$', views.user_login, name='user_login'),
    url(r'^regist$', views.regist, name='regist'),
    url(r'^create_user$', views.create_user, name='create_user'),
    url(r'^show/(?P<id>\d+)$', views.show, name='show'),
    url(r'^jobs$', views.jobs, name='jobs'),
]
