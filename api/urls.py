from django.urls import include, path
from django.conf.urls import url

from models.rooms import room_api
from models.move import move_api
from models.players import players_api


urlpatterns = [
    path("", include("rest_auth.urls")),
    path("registration/", include("rest_auth.registration.urls")),
    path("room/", room_api),
    path("room/players", players_api),
    path("move/", move_api),
]
