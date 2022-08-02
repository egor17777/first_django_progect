from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_horoscope'),
    path('type', views.type_index),
    path('test', views.test),
    path('type/<str:type>', views.get_zodiac_list_in_type,name= "type-zodiac"),
    path('<int:signs_zodiac>', views.get_info_signs_zodiac_number),
    path('<str:signs_zodiac>', views.get_info_signs_zodiac,name="name-horoscope"),
    
]
