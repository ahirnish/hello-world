from django.conf.urls import url

from .views import index, index1

urlpatterns = [
    url(r'^ahirnish/', index),
    url(r'^axunna/', index1),
]
