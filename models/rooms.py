from django.http import JsonResponse


def room_api(request, *args, **kwargs):
    return JsonResponse({"a": 1})
