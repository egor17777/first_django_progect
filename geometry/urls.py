from django.urls import path
from . import views
from django.http import HttpResponseRedirect


urlpatterns = [
    path('rectangle/<int:widht>/<int:height>', views.get_rectangle_area,name="redirect_1"),
    path('square/<int:widht>', views.get_square_area, name="redirect_2"),
    path('circle/<int:radius>', views.get_circle_area,name="redirect_3"),
    path('get_rectangle_area/<int:widht>/<int:height>', views.redirect_function_1),
    path('get_square_area/<int:widht>', views.redirect_function_2,),
    path('get_circle_area/<int:radius>', views.redirect_function_3)
]
