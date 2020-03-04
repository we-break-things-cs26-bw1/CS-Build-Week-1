from django.urls import include, path
from django.conf.urls import url
from .views import room_list, room_detail

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('room/', room_list),
    path('room/<int:pk>/', room_detail),
]
