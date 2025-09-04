from django.urls import path
from .views import ListCart, ListCategory, DetailCategory, ListBook, DetailBook, ListProduct, DetailProduct, DetailCart


urlpatterns = [
    # Categories
    path('categories',ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>',DetailCategory.as_view(), name='category-detail'),
    # now for the books 
    path('books',ListBook.as_view(), name='books'),
    path('books/<int:pk>',DetailBook.as_view(), name='book-detail'),
    # now for the products
    path('products',ListProduct.as_view(), name='products'),
    path('products/<int:pk>',DetailProduct.as_view(), name='product-detail'),
    # now for the carts
    path('carts',ListCart.as_view(), name='carts'),
    path('carts/<int:pk>',DetailCart.as_view(), name='cart-detail'),
]
