from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


def vj_response(data, status=HTTP_200_OK):
    return Response({"success": True, "result": data}, status=status)
