from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat!",
    "february": "Walk for at least 20 minutes per day!",
    "march": "Learn Django at least for 30 minutes!",
    "april": "Read a new book for 15 minutes every day!",
    "may": "Try a new recipe each week!",
    "june": "Spend 10 minutes meditating daily!",
    "july": "Drink at least 2 liters of water every day!",
    "august": "Do 15 minutes of stretching exercises daily!",
    "september": "Wake up 30 minutes earlier than usual!",
    "october": "Write down three things you are grateful for each day!",
    "november": "Avoid sugar for 15 days!",
    "december": "Reflect on and document the year's biggest lessons!"
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capit_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capit_month}</a></li>"

    reponse_data = f"<ul>{list_items}</ul>"

    return HttpResponse(reponse_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    # builds /challenge/<month>
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"

        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
