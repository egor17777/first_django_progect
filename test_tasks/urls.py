from django.urls import path
from . import views

urlpatterns = [
    path('test2',views.get_guinness_world_records),
    path('test1',views.test1),
]
