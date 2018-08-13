from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.marksheet_list,
        name='marksheet-list'),
    url(r'^marksheet/(?P<pk>\d+)/$', views.MarksheetDetailView.as_view(),
        name='marksheet-detail'),

]
