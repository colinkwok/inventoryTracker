from django.db import models

# Create your models here.
class InventoryItem(models.Model):
    item_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    item_description = models.CharField(max_length=500)
    stock_quantity = models.IntegerField(default=0)
    item_location = models.CharField(max_length=50)
    release_date = models.DateTimeField('release date')

    def __str__(self):
        return self.company + ": " + self.item_name

