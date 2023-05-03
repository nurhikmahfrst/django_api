from rest_framework import serializers
from . models import Jadwal

class jadwalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jadwal
        fields = "__all__"
