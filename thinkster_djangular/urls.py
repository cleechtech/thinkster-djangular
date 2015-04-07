from django.conf.urls import patterns, url

from thinkster_djangular.views import IndexView

urlpatterns = patterns(
    '',

    url('^.*$', IndexView.as_view(), name='index'),
)
