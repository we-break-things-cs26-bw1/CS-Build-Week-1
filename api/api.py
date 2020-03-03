from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json


@csrf_exempt
@api_view(["GET"])
def initPlayer(request):
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    players = room.playerNames(player_id)
    # room  willpresumedly contain references
    #  to monsters, items, interactive  event
    # exits = room.validExits
    players = room.playerNames(player_id)
    return JsonResponse({'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players}, safe=True)

@csrf_exempt
@api_view(["POST"])
def playerInteract(request):
    player = request.user.player
    action = request.value
    # result = gameLoop.doThing(player, action)
    result = "TODO"
    if result.valid:
        return JsonResponse({"valid":"result"})
    else:
        return JsonResponse({"error":"error"})

@csrf_exempt
@api_view(["POST"])
def playerMove(request):
    player = request.user.player
    move = request.value
    moveResult = "todo"  # gameLoop.move(player, move)
    if moveResult.valid:
        newRoom = moveResult.newRoom()
        interactionOptions = newRoom.interactionOptionsForRoom
        exits = newRoom.exits
        return JsonResponse({"valid":"result"})
        # describing newroom, interactionOptions)
    else:
        return JsonResponse({"error":"error"})
