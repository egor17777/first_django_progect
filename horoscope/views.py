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

    li_elements = ''

    for i in zodiacs:
        redirect_path = reverse("name-horoscope", args=[i])
        li_elements += f"<li><a href= {redirect_path}>{i.title()}</a></li>"
    li_elements += f"<li><a href= /horoscope/type>Types sign zodiac</a></li>"
    response_html = f"<ul>{li_elements}</ul>"

    return HttpResponse(response_html)


def get_info_signs_zodiac(request, signs_zodiac: str | int) -> HttpResponse:
    """Gives information on the signs of the zodiac

    Args:
        request (_type_): _description_
        signs_zodiac (str | int): Accepts either a zodiac sign or its number

    Returns:
        HttpResponse: Returns the response to the page
    """
    if isinstance(signs_zodiac, int):
        zodiacs = list(dict_zodiac)
        if signs_zodiac <= len(zodiacs):
            name_zodiac = zodiacs[signs_zodiac-1]
            redirect_url = reverse("name-horoscope", args=(name_zodiac, ))
            return HttpResponseRedirect(redirect_url)
        else:
            return HttpResponseNotFound(f'Oops... I can\'t find that number zodiac sign "{signs_zodiac}"')
    description = dict_zodiac.get(signs_zodiac, None)
    if description:
        return HttpResponse(f"<h1>Sign zodiac: {description}</h1>")
    else:
        return HttpResponseNotFound(f'Oops... I can\'t find that zodiac sign "{signs_zodiac}"')


def test(request):
    response = render_to_string("horoscope/index_page.html")
    return HttpResponse(response)
    
