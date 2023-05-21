from rest_framework import serializers
from .models import Categories


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField()
    thumbnail = serializers.ImageField();
    class Meta:
        model = Categories
        fields = '__all__'