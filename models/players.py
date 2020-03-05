from django.http import JsonResponse


def players_api(request, *args, **kwargs):
    return JsonResponse({"a": 1})
