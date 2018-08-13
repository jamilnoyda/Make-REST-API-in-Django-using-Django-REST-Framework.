from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^$', views.profile, name="profile"),
    url(r'^login/$', auth_views.login,
        {'redirect_authenticated_user': True}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),

]
