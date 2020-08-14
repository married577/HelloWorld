from django.db import models


# Create your models here.
class Book(models.Model):
    b_name = models.CharField(max_length=32)
    b_price = models.FloatField(default=1)


class Desk(models.Model):
    d_height = models.IntegerField(default=70)

    # @classmethod
    # def create(cls, d_height=800):
    #     desk = cls()
    #     desk.d_height = d_height
    #     desk.save()

    class Meta:
        db_table = 'desk'
        # 排序需要元组或者列表类型，加，变成元组类型，加-变成降序
        ordering = "-d_height",


class Reader(models.Model):
    r_name = models.CharField(max_length=16, unique=True)  # unique=True是唯一
    r_pwd = models.CharField(max_length=128)
