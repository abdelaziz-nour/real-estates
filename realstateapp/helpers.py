

from django.http import JsonResponse


def custom_response(data=None, error=None, message=None):
    return JsonResponse(
        {
            'data': data,
            "message": message
        }
    )
