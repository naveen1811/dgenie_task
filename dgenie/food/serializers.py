from rest_framework import serializers
from food.models import Food

__author__ = 'naveen'


class FoodSerializers(serializers.ModelSerializer):
    restaurant_name = serializers.Field(source='get_restaurant_name')
    restaurant_rating = serializers.Field(source='get_restaurant_rating')
    restaurant_service = serializers.Field(source='get_restaurant_service')


    class Meta:
        model = Food
        exclude = ['id', 'is_addon_must', 'restaurant']
