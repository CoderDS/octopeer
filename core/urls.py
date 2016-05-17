from django.conf.urls import url, include
from core import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^repositories/$', views.RepositoryList.as_view(), name='repository-list'),
    url(r'^repositories/(?P<owner>.+)/(?P<name>.+)/$', views.RepositoryDetail.as_view(), name='repository-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<username>.+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^pullrequests/$', views.PullRequestList.as_view(), name='pullrequest-list'),
    url(r'^pullrequests/(?P<pk>[0-9]+)/$', views.PullRequestDetail.as_view(), name='pullrequest-detail'),
]
