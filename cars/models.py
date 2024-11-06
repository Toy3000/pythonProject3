from django.db import models

class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=50)
    price = models.IntegerField()
    year = models.IntegerField()
