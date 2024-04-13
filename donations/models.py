from django.db import models

from accounts.models import Provider, Charity
from products.models import Product


# This module contains all the models for the donations
class Donation(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    is_accepted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.provider.user.name} -> {self.charity.user.name}"

    class Meta:
        db_table = 'donations'


class DonationItem(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    expiration_date = models.DateField()
    is_perishable = models.BooleanField()

    def __str__(self):
        return f"{self.product} ({self.quantity}) in {self.donation}"

    class Meta:
        db_table = 'donation_items'

