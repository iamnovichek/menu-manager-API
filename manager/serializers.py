from rest_framework import serializers
from .models import *


class FirstCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstCourse
        fields = '__all__'


class SecondCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondCourse
        fields = '__all__'


class DessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dessert
        fields = '__all__'


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'
