from rest_framework import serializers

from member.models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        read_only = ['is_active']