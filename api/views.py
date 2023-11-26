from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_auth(request: Request) -> Response:
    ...
