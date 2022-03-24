from rest_framework import serializers

from parking_api.apps.parking.models import Parking
from parking_api.apps.parking.utils import humanize_timedelta


class ParkingSerializer(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()

    def get_time(self, obj) -> str:
        return humanize_timedelta(obj.time)

    class Meta:
        model = Parking
        fields = "__all__"
