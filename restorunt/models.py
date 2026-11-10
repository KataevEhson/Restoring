from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)




class Dish(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.BigIntegerField()




class Table(models.Model):
    number = models.IntegerField()



class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    created_at = models.CharField()

