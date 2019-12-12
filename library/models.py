from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=256)


class Reader(models.Model):
    name = models.CharField(max_length=256)
    books = models.ManyToManyField(Book, related_name='books', through='BooksReaders')


class BooksReaders(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
