from django.db import models

# Create your models here.


#Restaurant model contains all the restaurant details
class Restaurant(models.Model):
    rest_id = models.IntegerField(max_length=10, db_index=True)
    name = models.CharField(max_length=300, db_index=True)
    rating = models.CharField(max_length=10, null=True, blank=True)
    service = models.CharField(max_length=300, db_index=True)

    def __unicode__(self):
        return "{}-{}".format(self.name, self.rest_id)



#Food details contains in this model
class Food(models.Model):
    restaurant = models.ForeignKey('Restaurant', related_name='food', db_index=True)
    item_id = models.IntegerField(max_length=10, db_index=True)
    dish = models.CharField(max_length=1000, db_index=True)
    price = models.IntegerField(max_length=5)
    item_sid = models.IntegerField(max_length=10, db_index=True)
    is_addon_must = models.BooleanField(default=False)


    def __unicode__(self):
        return "{}-{}".format(self.dish, self.item_id)

    def get_restaurant_rating(self):
        return self.restaurant.rating

    def get_restaurant_name(self):
        return self.restaurant.name

    def get_restaurant_service(self):
        return self.restaurant.service
