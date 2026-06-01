from rest_framework import serializers

from subscription.models import GymMembership, Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        read_only = ['is_active', 'created_at','updated_at']




class GymMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymMembership
        fields = '__all__'
        read_only = ['created_at','updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance) 
        data['member'] = instance.member.first_name
        data['subsrciption']=instance.subscription.name
        data['trainer']=[instance.trainer.full_name if instance.trainer is not None else None]
        return data
    
    def create(self, validated_data):
        print(validated_data)
        one_day_price = validated_data['subsrciption'].price / validated_data['subsrciption'].days
        validated_data['price']=validated_data['days']*one_day_price
        return super().create(validated_data)