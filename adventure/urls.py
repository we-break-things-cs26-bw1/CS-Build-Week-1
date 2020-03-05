from django.conf.urls import url
from .api import *

urlpatterns = [
    url('init', initialize),
    url('move', move),
    url('say', say),
    url('sauce',sauce)
]
