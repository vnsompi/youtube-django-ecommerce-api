from rest_framework import serializers
from .models import Product, Category, Book, Cart
from  django.contrib.auth.models import User




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


class CartUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')



class CartSerializer(serializers.ModelSerializer):
    cart_id = CartUserSerializer(read_only=True, many=False )
    books = BookSerializer(many=True, read_only=True)
    # cela veut dire que chaque fois qu'on va serialiser un cart, on va aussi serialiser les books lies a ce cart
    products = ProductSerializer(many=True, read_only=True)
    # cela veut dire que chaque fois qu'on va serialiser un cart, on va aussi serialiser les products lies a ce cart
    class Meta:
        model = Cart
        fields = ('cart_id', 'created_at', 'books', 'products')