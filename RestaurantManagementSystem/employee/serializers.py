from rest_framework import serializers
from .models import Waiter


class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Waiter
        fields= "__all__"

