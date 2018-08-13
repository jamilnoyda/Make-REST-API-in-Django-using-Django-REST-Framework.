from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="teachers"),
    url(r'^marksheet/(?P<pk>\d+)/$',
        views.MarksheetDetailView.as_view(), name='marksheet-detail'),
    url(r'^marksheet/$', views.MarksheetListView.as_view(),
        name='marksheet-list'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^standard/$', views.standard, name='standard'),

]
