import logging
from django.core import exceptions
from rest_framework import exceptions as rest_exceptions
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import exception_handler

logger = logging.getLogger("django")


def vj_api_exception_handler(exc, context):
    if isinstance(exc, exceptions.ValidationError):
        return JsonResponse(
            {"success": False, "result": exc.message},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if isinstance(exc, rest_exceptions.ValidationError):
        response = exception_handler(exc, context)
        if isinstance(response.data, list):
            return JsonResponse(
                {"success": False, "result": response.data[0]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for key, value in response.data.items():
            if isinstance(value, list):
                if isinstance(value[0], dict):
                    for k, v in value[0].items():
                        if isinstance(v, list):
                            message = " ".join([str(e) for e in v])
                            break
                        else:
                            message = v
                            break
                else:
                    message = " ".join([str(elem) for elem in value])
                    break
            else:
                message = value
        return JsonResponse(
            {"success": False, "result": message}, status=status.HTTP_400_BAD_REQUEST
        )
    # Client should never throw an actual PermissionDenied, and we need the 401
    if isinstance(exc, exceptions.PermissionDenied):
        return JsonResponse(
            {"success": False, "result": str(exc)}, status=status.HTTP_401_UNAUTHORIZED
        )

    if isinstance(exc, KeyError):
        return JsonResponse(
            {"success": False, "result": "Missing Key: {0}".format(exc)},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Order on this as we are overriding the above exceptions.
    response = exception_handler(exc, context)
    if response:
        if not "success" in response.data and not "result" in response.data:
            try:
                return JsonResponse(
                    {"success": False, "result": exc.detail}, status=exc.status_code
                )
            except AttributeError:
                return JsonResponse(
                    {"success": False, "result": exc.args[0]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            logger.exception(exc)
            return response

    logger.exception(exc)
    return JsonResponse(
        {"success": False, "result": str(exc)},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
