from django.shortcuts import render
from rest_framework import generics
from .models import Category, Book, Product
from .serializers import *


class ListCategory(generics.ListCreateAPIView):
     queryset = Category.objects.all()
     serializer_class = CategorySerializers

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
     queryset = Category.objects.all()
     serializer_class = CategorySerializers

class ListBook(generics.ListCreateAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializers

class DetailBook(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class ListProduct(generics.ListCreateAPIView):
     queryset = Product.objects.all()
     serializer_class = productserializers

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Product.objects.all()
    serializer_class = productserializers



    
        