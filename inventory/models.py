from django.db import models


class Inventory(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    user_id = models.IntegerField()

    def __str__(self):
        return self.product_name
