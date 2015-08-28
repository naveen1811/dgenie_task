from django.conf.urls import patterns, url
from food.views import FoodAPI

__author__ = 'naveen'

urlpatterns = patterns('food.views',
                       url(r'^search/$', FoodAPI.as_view()),
                )
