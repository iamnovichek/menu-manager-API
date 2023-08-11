from rest_framework import generics
from drf_multiple_model.views import ObjectMultipleModelAPIView
from .models import FirstCourse, SecondCourse, Drink, Dessert
from .serializers import (SecondCourseSerializer, FirstCourseSerializer,
                          DessertSerializer, DrinkSerializer)


class ListMenuView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': FirstCourse.objects.all(), 'serializer_class': FirstCourseSerializer},
        {'queryset': SecondCourse.objects.all(), 'serializer_class': SecondCourseSerializer},
        {'queryset': Dessert.objects.all(), 'serializer_class': DessertSerializer},
        {'queryset': Drink.objects.all(), 'serializer_class': DrinkSerializer}
    ]


class ListFirstCoursesView(generics.ListAPIView):
    serializer_class = FirstCourseSerializer
    queryset = FirstCourse.objects.all()


class CFirstCourseView(generics.ListCreateAPIView):
    serializer_class = FirstCourseSerializer
    queryset = FirstCourse.objects.all()


class RUDFirstCourseView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FirstCourseSerializer
    queryset = FirstCourse.objects.all()


class ListSecondCoursesView(generics.ListAPIView):
    serializer_class = SecondCourseSerializer
    queryset = SecondCourse.objects.all()


class CSecondCourseView(generics.ListCreateAPIView):
    serializer_class = SecondCourseSerializer
    queryset = SecondCourse.objects.all()


class RUDSecondCourseView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SecondCourseSerializer
    queryset = SecondCourse.objects.all()


class ListDessertsView(generics.ListAPIView):
    serializer_class = DessertSerializer
    queryset = Dessert.objects.all()


class CDessertView(generics.ListCreateAPIView):
    serializer_class = DessertSerializer
    queryset = Dessert.objects.all()


class RUDDessertView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DessertSerializer
    queryset = Dessert.objects.all()


class ListDrinksView(generics.ListAPIView):
    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()


class CDrinkView(generics.ListCreateAPIView):
    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()


class RUDDrinkView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()
