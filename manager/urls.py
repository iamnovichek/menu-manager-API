from django.urls import path
from .views import *

urlpatterns = [
    path('c-first-course/', CFirstCourseView.as_view()),
    path('rud-first-course/<int:pk>', RUDFirstCourseView.as_view()),
    path('list-first-course/', ListFirstCoursesView.as_view()),
    path('c-second-course/', CSecondCourseView.as_view()),
    path('rud-second-course/<int:pk>', RUDSecondCourseView.as_view()),
    path('list-second-course/', ListSecondCoursesView.as_view()),
    path('c-dessert/', CDessertView.as_view()),
    path('rud-dessert/<int:pk>', RUDDessertView.as_view()),
    path('list-dessert/', ListDessertsView.as_view()),
    path('c-drink/', CDrinkView.as_view()),
    path('rud-drink/<int:pk>', RUDDrinkView.as_view()),
    path('list-drink/', ListDrinksView.as_view()),
    path('list-menu/', ListMenuView.as_view())
]
