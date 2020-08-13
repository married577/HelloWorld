from django.db import models


# Create your models here.
class Book(models.Model):
    b_name = models.CharField(max_length=32)
    b_price = models.FloatField(default=1)


class Desk(models.Model):
    d_height = models.IntegerField(default=70)

    class Meta:
        db_table = 'desk'
