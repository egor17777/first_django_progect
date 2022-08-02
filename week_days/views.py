from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

week_day_plan_dict = {
    "monday": ["Wake up", "Wash your face", "Brush your teeth", "Have breakfast"],
    "tuesday": ["Wake up", "Brush your teeth", "Wash your face", "Have breakfast", "Study", "Clean the house"]
}

def index(request):
    return render(request, 'week_days/greeting.html')

def get_plans_for_the_day(request, day_of_the_week: str) -> HttpResponse:
    """Returns to HttpResponse plans for the day

    Args:
        request (_type_): request
        day_of_the_week (str): Day of the week

    Returns:
        HttpResponse: Returns the response to the page
    """
    description = week_day_plan_dict.get(day_of_the_week, None)
    data = {
        "day" : day_of_the_week,
        "task" : description
    }
    return render(request, "week_days/tasks.html",context=data)


def get_day_of_the_week(request, day_of_the_week: int) -> HttpResponse:
    """Returns day of the week

    Args:
        request (_type_): _description_
        day_of_the_week (int): day of the week

    Returns:
        HttpResponse: _description_
    """
    list_day_of_the_week = list(week_day_plan_dict)

    if day_of_the_week <= len(list_day_of_the_week):
            name_day = list_day_of_the_week[day_of_the_week-1]
            redirect_url=reverse("name_day_week", args=(name_day, ))
            return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'<h2>Oops... Invalid day number "{day_of_the_week}"</h2>')
