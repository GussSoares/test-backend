from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class CustomView:
    authentication_classes = []
    permission_classes = []
    response = Response

    def _response_200(self, **kwargs) -> Response:
        return Response(kwargs, status=status.HTTP_200_OK)

    def _response_201(self, **kwargs) -> Response:
        return Response(kwargs, status=status.HTTP_201_CREATED)

    def _response_400(self, **kwargs) -> Response:
        return Response(kwargs, status=status.HTTP_400_BAD_REQUEST)

    def _response_404(self, **kwargs) -> Response:
        return Response(kwargs, status=status.HTTP_404_NOT_FOUND)

    def _response_409(self, **kwargs) -> Response:
        return Response(kwargs, status=status.HTTP_409_CONFLICT)

    def _response_500(self, **kwargs) -> Response:
        return Response(kwargs, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def _response_501(self, **kwargs) -> Response:
        return Response(kwargs, status=status.HTTP_501_NOT_IMPLEMENTED)


class CustomAPIViewSet(GenericViewSet, CustomView):
    ...
