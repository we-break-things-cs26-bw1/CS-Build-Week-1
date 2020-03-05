from django.http import JsonResponse


def move_api(request, *args, **kwargs):
    return JsonResponse({"a": 1})
