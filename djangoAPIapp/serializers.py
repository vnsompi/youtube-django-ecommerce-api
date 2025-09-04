from rest_framework import serializers
from .models import Product, Category, Book




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title' ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'category', 'isbn', 'pages', 'stock','imageUrl', 'date_created', 'status', 'author']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_tag', 'name', 'price', 'category', 'stock', 'imageUrl', 'status', 'date_created']

