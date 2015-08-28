from django.contrib import admin

# Register your models here.
from food.models import Restaurant, Food


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('rest_id', 'name', 'service', 'rating')
    search_fields = ['rest_id', 'name', 'service']
    list_filter = ['name', 'service']


class FoodAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'dish', 'price', 'item_sid')
    search_fields = ['item_id', 'dish', 'item_sid']
    list_filter = ['dish']


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)