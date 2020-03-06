from django.contrib import admin
from .models import Room
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'n_to', 's_to', 'e_to', 'w_to']

# Adds Room to the admin view.
admin.site.register(Room, RoomAdmin)
