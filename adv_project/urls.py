from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

from pages.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    path('', home_view, name='home'),
]
