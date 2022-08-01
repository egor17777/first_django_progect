from django.urls import path
from . import views

urlpatterns = [
    path('<int:day_of_the_week>', views.get_day_of_the_week),
    path('<str:day_of_the_week>', views.get_plans_for_the_day, name="name_day_week"),
]
