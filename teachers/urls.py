from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'marksheet/(?P<pk>\d+)/$',
        views.MarksheetDetailView.as_view(), name='marksheet-detail'),
    url(r'marksheet/$', views.MarksheetListView.as_view(),
        name='marksheet-list'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'$', views.home, name="teachers"),
]
