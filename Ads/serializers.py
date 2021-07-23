from rest_framework import serializers
from .models import Channel, Discount



class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'
#
#
class DiscountSerializer(serializers.ModelSerializer):
    channels = ChannelSerializer()
    class Meta:
        model = Discount
        fields = '__all__'


#
# class DiscountSerializer(serializers.Serializer):
#     channels = ChannelSerializer()
#     percent = serializers.IntegerField()
#     min_days = serializers.IntegerField()
