from rest_framework import serializers
from .models import Book, Monitor

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "name", "image", "description", "checkout_date", "return_date")
        
class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = ("id", "name", "image", "description", "checkout_date", "return_date")
