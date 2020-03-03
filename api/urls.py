from django.urls import include, path
from django.conf.urls import url

from api.api import initPlayer, playerInteract, playerMove

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    url('initPlayer', initPlayer),
    url('player_interact', playerInteract),
    url('player_move', playerMove),
]
