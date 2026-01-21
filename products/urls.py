from django.urls import path, re_path
from django.views.generic.base import RedirectView

from .views import (
    ProductCreateView,
    ProductDetailView,
    ProductDownloadView,
    ProductListView,
    ProductUpdateView,
    ProductRatingAjaxView,
    VendorListView,
    )

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('vendor/', VendorListView.as_view(), name='vendor_list'),
    re_path(r'^vendor/(?P<vendor_name>[\w.@+-]+)/$', VendorListView.as_view(), name='vendor_detail'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='detail_slug'),
    path('<int:pk>/download/', ProductDownloadView.as_view(), name='download'),
    re_path(r'^(?P<slug>[\w-]+)/download/$', ProductDownloadView.as_view(), name='download_slug'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='update'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', ProductUpdateView.as_view(), name='update_slug'),
    path('ajax/rating/', ProductRatingAjaxView.as_view(), name='ajax_rating'),
]
