from rest_framework import serializers

from library.models import Book, Reader


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'
        depth = 1
