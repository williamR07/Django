from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk at least for 20 minutes a every day!",
    "march": "Learn django at least 20 minutes a day",
    "april": "Its april foools",
    "may": "Hello from the month of may",
    "june": "Eat no meat for the entire month!",
    "july": "Walk at least for 20 minutes a every day!",
    "august": "Learn django at least 20 minutes a day",
    "september": "Eat no meat for the entire month!",
    "ocotober": "Walk at least for 20 minutes a every day!",
    "november": "Learn django at least 20 minutes a day",
    "december": "Christmas is soon"

}
# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{
            capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Month is not supported :(</h1>")
