from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses/', views.courses, name='courses'),
    url(r'^course/(?P<pk>\d+)/$', views.course, name='course'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^addcourse/', views.addcourse, name='addcourse'),
    url(r'^search/$', views.search),
    ]
