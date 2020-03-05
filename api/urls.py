from django.urls import include, path
from django.conf.urls import url
from .views import room_list, room_detail

from models.rooms import room_api
from models.move import move_api
from models.players import players_api


urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('dungeon/', room_list),
    path('dungeon/<int:pk>/', room_detail),
]
