from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<code>([A-Z]){2}.[0-9]{3}.[0-9]{3})/$', views.detail, name='detail'),
]