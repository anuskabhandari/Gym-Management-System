from rest_framework import serializer
from txn.models import TXN


class TXNSerializer(serializer.ModelSerializer):
    class Meta:
        model = TXN
        fields = '__all__'