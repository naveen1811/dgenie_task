from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

import json
from rest_framework.views import APIView
from food.models import Food, Restaurant
from food.serializers import FoodSerializers
from rest_framework.response import Response


#populate the json data into database
def get_json_data():
    json_file = open('/Users/naveen/Downloads/food.json').read()
    data = json.loads(json_file)
    try:
        if 'results' in data:
            for i in range(0, len(data['results'])):
                restaurant_rating = data['results'][i]['restaurant_rating']
                restaurant_name = data['results'][i]['restaurant_name']
                service = data['results'][i]['service']
                rest_id = data['results'][i]['rest_id']
                rest = Restaurant.objects.create(rating=restaurant_rating, rest_id=rest_id,
                                                 service=service, name=restaurant_name)
                for j in range(0, len(data['results'][i]['restaurant_food'])):
                    item_id = data['results'][i]['restaurant_food'][j]['item_id']
                    dish = data['results'][i]['restaurant_food'][j]['dish']
                    price = data['results'][i]['restaurant_food'][j]['price']
                    item_sid = data['results'][i]['restaurant_food'][j]['item_sid']
                    is_addon_must = data['results'][i]['restaurant_food'][j]['is_addon_must']
                    Food.objects.create(restaurant=rest, item_id=item_id, dish=dish, price=price, item_sid=item_sid,
                                            is_addon_must=is_addon_must)
    except Exception as e:
        print e


#API to get the restaurant data
class FoodAPI(APIView):

    def get(self, request):
        try:
            dish = request.GET['food']
            service = request.GET['service']
            queryset = Food.objects.filter(dish__icontains=dish, restaurant__service=service).distinct('item_id')
            serialized = FoodSerializers(queryset, many=True)
            return Response(serialized.data)
        except Exception as e:
            return HttpResponse(e)







