from django.conf.urls import url

from . views import (
    SosmedListView,
    DeleteView,
    SosmedView,
    )

urlpatterns = [
    url(r'^update/(?P<update_id>[0-9]+)$', SosmedView.as_view(mode='update'), name='update'),
    url(r'^create/$', SosmedView.as_view(), name='create'),
    url(r'^delete/(?P<delete_id>[0-9]+)$', DeleteView.as_view(), name='delete'),
    url(r'^$', SosmedListView.as_view(), name='list'),
]
