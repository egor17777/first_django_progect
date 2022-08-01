from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from math import pi

from django.urls import reverse

# Create your views here.


def get_rectangle_area(request, widht: int, height: int) -> HttpResponse:
    """Returns the area of a rectangle

    Args:
        request (_type_): _description_
        widht (int): widht
        height (int): height

    Returns:
        HttpResponse: Returns the response to the page
    """
    return HttpResponse(f"The area of a {widht} by {height} rectangle is {widht*height} ")


def get_square_area(request, widht: int) -> HttpResponse:
    """Returns the area of a square

    Args:
        request (_type_): _description_
        widht (int): widht

    Returns:
        HttpResponse: Returns the response to the page
    """
    return HttpResponse(f"The area of a {widht} by {widht} square is {widht**2} ")


def get_circle_area(request, radius: int) -> HttpResponse:
    """Returns the area of a circle

    Args:
        request (_type_): _description_
        radius (int): radius

    Returns:
        HttpResponse: Returns the response to the page
    """
    return HttpResponse(f"The area of a circle with a radius of {radius} is {round(pi*radius**2,2)} ")


"""Redirect functions"""


def redirect_function_1(request, widht, height):
    redirect_url_1= reverse("redirect_1", args=(widht,height))
    return HttpResponseRedirect(redirect_url_1)


def redirect_function_2(request, widht):
    redirect_url_2= reverse("redirect_2", args=(widht, ))
    return HttpResponseRedirect(redirect_url_2)


def redirect_function_3(request, radius):
    redirect_url_3= reverse("redirect_3", args=(radius, ))
    return HttpResponseRedirect(redirect_url_3)
