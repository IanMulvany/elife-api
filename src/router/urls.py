from django.conf.urls import patterns, include, url
from router import views

urlpatterns = patterns('',
    url(r'v1/(?P<arg1>[a-zA-Z]{1,3})/(?P<arg2>\d{1,5})/', views.example_route),
)

