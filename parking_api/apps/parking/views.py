from datetime import datetime, timezone

from parking_api.apps.core import views
from parking_api.apps.parking.models import Parking
from parking_api.apps.parking.serializers import ParkingSerializer
from parking_api.apps.parking.utils import PlateValidatior


class ParkingView(views.CustomAPIViewSet):
    """
    API endpoint that make reservation in the parking
    """

    queryset = Parking.objects.get_queryset()
    serializer_class = ParkingSerializer
    authentication_classes = []
    permission_classes = []

    def _get_parking(self, pk: int) -> Parking:
        try:
            return Parking.objects.get(pk=pk)
        except Parking.DoesNotExist:
            return None

    def _get_parking_by_plate(self, plate: str):
        try:
            return Parking.objects.filter(plate=plate)
        except Parking.DoesNotExist:
            return self.queryset

    def enter(self, request, *args, **kwargs):
        if PlateValidatior.validate(request.data.get("plate")):
            reservation: Parking = self.queryset.create(
                plate=request.data.get("plate"),
            )
        else:
            return self._response_400(
                message="Provide a valid plate in AAA-9999 format!",
            )
        return self._response_201(
            message="welcome to parking!", reservation=reservation.id
        )

    def out(self, request, pk: int, *args, **kwargs):
        if parking := self._get_parking(pk):
            if parking.left:
                return self._response_200(message="It's already out!")

            if parking.paid:
                parking.time = datetime.now(tz=timezone.utc) - parking.created
                parking.left = True
                parking.save()
                return self._response_200(message="Bye, see you later!")

            else:
                return self._response_400(message="To exit, please pay.")
        else:
            return self._response_404(message="Not found!")

    def payment(self, request, pk: int, *args, **kwargs):
        if parking := self._get_parking(pk):
            if parking.paid:
                return self._response_200(message="It's already paid!")
            else:
                parking.paid = True
                parking.save()
                return self._response_200(message="Paid!")
        else:
            return self._response_404(message="Not found!")

    def history(self, request, plate: str, *args, **kwargs):
        if PlateValidatior.validate(plate):
            if hist := self._get_parking_by_plate(plate):
                result = self.serializer_class(hist, many=True)
                return self._response_200(message="Success", data=result.data)
            else:
                return self._response_404(
                    message=f"Vehicle with plate '{plate}' does not registred",
                )
        else:
            return self._response_400(
                message="Provide a valid plate in AAA-9999 format!",
            )
