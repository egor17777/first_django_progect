from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def test1(request):
    data={
        "уеаг_born" : 1964,
        "city_born" : "Kharkiv",
        "movie_name" : "On the crest of a wave"

    }
    return render(request, "test_tasks/task_1.html", context=data)

def get_guinness_world_records(request) :
    context = {
    'power_nan': 'Narve Laeret',
    'bar_name': 'Bob’s BBQ & Grill',    
    'count_needle': 1799,
    }

    return render(request, 'test_tasks/task_2.html', context=context)