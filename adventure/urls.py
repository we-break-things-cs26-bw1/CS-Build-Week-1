from django.conf.urls import url
from .api import *
from .clientex import NameFormView
urlpatterns = [
    url('init', initialize),
    url('move', move),
    url('say', say),
    url('sauce',sauce),
    url(r'^name/', NameFormView.as_view()),
]
