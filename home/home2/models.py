from django.db import models
from django.utils import timezone

class House(models.Model):
    url = models.URLField(unique=True)
    description = models.TextField()
    log = models.TextField(blank=True)
    n_bedrooms = models.PositiveSmallIntegerField()
    reception = models.BooleanField()
    distance_to_station_km = models.FloatField()
    postcode = models.CharField(max_length=8, blank=True)
    garden = models.BooleanField()
    carpet = models.BooleanField()
    ng_valuation = models.IntegerField(null=True, blank=True)
    ne_valuation = models.IntegerField(null=True, blank=True)
    land_registry_price_sold = models.IntegerField(null=True, blank=True)
    deactivated = models.DateField(null=True, blank=True)
    first_call_on = models.DateField(null=True, blank=True)
    first_visit_on = models.DateField(null=True, blank=True)
    lease = models.PositiveSmallIntegerField(null=True, blank=True)

    @property
    def asking_price(self):
        return self.prices.latest('date').price

    @property
    def current_offer(self):
        return self.offers.latest('date').amount

    def __str__(self):
        return self.description


class HousePrice(models.Model):
    house = models.ForeignKey(House, on_delete=models.PROTECT, related_name='prices')
    date = models.DateField(default=timezone.now)
    price = models.IntegerField()

    class Meta:
        unique_together = (('house', 'date'),)

class HouseOffer(models.Model):
    house = models.ForeignKey(House, on_delete=models.PROTECT, related_name='offers')
    date = models.DateField(default=timezone.now)
    amount = models.IntegerField()

    class Meta:
        unique_together = (('house', 'date'),)
