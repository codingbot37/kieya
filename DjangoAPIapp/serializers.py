from rest_framework import serializers
from .models import *
class CategorySerializers(serializers.ModelSerializer):

  class Meta:
    fields = '__all__'
    model = Category


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Book


class productserializers(serializers.ModelSerializer):        
  class Meta:
      fields = '__all__'
      model = Product    












            