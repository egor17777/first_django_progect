from unicodedata import name
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
# Create your views here.

dict_zodiac = {
    "aries": "Aries (March 21 – April 19)",
    "taurus": "Taurus (April 20 – May 20)",
    "gemini": "Gemini (May 21 – June 20)",
    "cancer": "Cancer (June 21 – July 22)",
    "leo": "Leo (July 23 – August 22)",
    "virgo": "Virgo (August 23 – September 22)",
    "libra": "Libra (September 23 – October 22)",
    "scorpio": "Scorpio (October 23 – November 21)",
    "sagittarius": "Sagittarius (November 22 – December 21)",
    "capricorn": "Capricorn (December 22 – January 19)",
    "aquarius": "Aquarius (January 20 – February 18)",
    "pisces": "Pisces (February 19 – March 20"

}

type_zodiac = {
    "fire": ["aries", "leo", "sagittarius"],
    "earth": ["taurus", "virgo", "capricorn"],
    "air": ["gemini", "libra", "aquarius"],
    "water": ["cancer", "scorpio", "pisces"]
}


def type_index(request):
    """Returns all type zodiac signs """
    types = list(type_zodiac)

    li_types = ''

    for i in types:
        redirect_path = reverse("type-zodiac", args=[i])
        li_types += f"<li><a href= {redirect_path}>{i.title()}</a></li>"
    response_html = f"<ul>{li_types}</ul>"

    return HttpResponse(response_html)


def get_zodiac_list_in_type(request, type):
    """Returns all zodiac signs of a given type"""
    zodiac_signs_in_type = type_zodiac.get(type, None)
    if zodiac_signs_in_type:
        types = list(zodiac_signs_in_type)

    li_types = ''

    for i in types:
        redirect_path = reverse("name-horoscope", args=[i.lower()])
        li_types += f"<li><a href= {redirect_path}>{i.title()}</a></li>"

    response_html = f"<ul>{li_types}</ul>"

    return HttpResponse(response_html)


def index(request):
    """Returns all signs zodiacs"""
    zodiacs = list(dict_zodiac)
    data = {
        "zodiacs" : zodiacs
    }

    return render(request, "horoscope/main_index.html", context=data)


def get_info_signs_zodiac(request, signs_zodiac: str) -> HttpResponse:
    """Gives information on the signs of the zodiac

    Args:
        request (_type_): _description_
        signs_zodiac (str): Accepts a zodiac sign 

    Returns:
        HttpResponse: Returns the response to the page
    """
    description = dict_zodiac.get(signs_zodiac, None)
    zodiacs = list(dict_zodiac)
    data = {
        "sign": signs_zodiac,
        "horoscope": description,
        "zodiacs" : zodiacs
    }
    return render(request, "horoscope/index_page.html", data)


def get_info_signs_zodiac_number(request, signs_zodiac: int) -> HttpResponseRedirect:
    """Accepts the serial number of the zodiac sign and redirects to the desired address

    Args:
        request (_type_): _description_
        signs_zodiac (int): Accepts a number zodiac sign 

    Returns:
        HttpResponseRedirect: Redirect
    """
    zodiacs = list(dict_zodiac)
    if signs_zodiac <= len(zodiacs):
        name_zodiac = zodiacs[signs_zodiac-1]
        redirect_url = reverse("name-horoscope", args=(name_zodiac, ))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'<h1>Oops... I can\'t find that number zodiac sign "{signs_zodiac}"</h1>')


def test(request):
    return render(request, "horoscope/index_page.html")
