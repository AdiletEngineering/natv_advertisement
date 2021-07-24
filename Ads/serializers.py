from rest_framework import serializers
from .models import Channel, Discount


class DiscountSerializer(serializers.ModelSerializer):
    # channels = ChannelSerializer()
    class Meta:
        model = Discount
        fields = ('min_days', 'percent')


class ChannelSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    image = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    discounts = DiscountSerializer(many=True)




#
# class DiscountSerializer(serializers.Serializer):
#     channels = ChannelSerializer()
#     percent = serializers.IntegerField()
#     min_days = serializers.IntegerField()
