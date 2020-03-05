from django.contrib import admin
from .models import Room
# Register your models here.

# class RoomAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'description', 'monster' , 'item', 'x', 'y','height', 'width', 'background', 'n', 's', 'e', 'w']

# Adds Room to the admin view.
admin.site.register(Room) #Would add ,RoomAdmin to the left of Room.
