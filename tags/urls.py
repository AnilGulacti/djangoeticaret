from django.urls import path, re_path

from .views import (
    TagDetailView,
    TagListView,
    )

app_name = 'tags'

urlpatterns = [
    path('', TagListView.as_view(), name='list'),
    re_path(r'^(?P<slug>[\w-]+)/$', TagDetailView.as_view(), name='detail'),
]
