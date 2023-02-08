from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=119)
    age = models.IntegerField()


class Publisher(models.Model):
    name = models.CharField(max_length=119)


class Book(models.Model):
    name = models.CharField(max_length=119)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()


class Store(models.Model):
    name = models.CharField(max_length=119)
    books = models.ManyToManyField(Book)
