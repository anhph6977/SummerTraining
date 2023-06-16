import traceback

from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    traceback.print_exc()
    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code
    return response
