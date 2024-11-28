from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Dictionary holding monthly challenges where the key is the month (in lowercase)
# and the value is the challenge text for that month.
monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk at least for 20 minutes a every day!",
    "march": "Learn django at least 20 minutes a day",
    "april": "Its april fools",
    "may": "Hello from the month of may",
    "june": "Eat no meat for the entire month!",
    "july": "Walk at least for 20 minutes a every day!",
    "august": "Learn django at least 20 minutes a day",
    "september": "Eat no meat for the entire month!",
    "october": "Walk at least for 20 minutes a every day!",
    "november": "Learn django at least 20 minutes a day",
    "december": None
}

# View function that handles the root URL (index).
# It lists all the months and links to their respective challenge pages.


def index(request):
    # Get the list of months (keys from the dictionary).
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

# View function that handles the month-based URL with the month number.
# It redirects the user to the appropriate month's challenge page.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())  # Get the list of months.

    # If the given month number is out of range, return a 404 error.
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    # Get the corresponding month name based on the month number.
    redirect_month = months[month - 1]

    # Use the reverse function to generate the URL for the month's challenge page.
    redirect_path = reverse("month-challenge", args=[redirect_month])

    # Redirect the user to the generated URL.
    return HttpResponseRedirect(redirect_path)

# View function that handles the month-based URL with the month name.
# It returns the challenge text for the specific month.


def monthly_challenge(request, month):
    try:
        # Try to get the challenge text for the given month.
        challenge_text = monthly_challenges[month]

        # Return the challenge text wrapped in an <h1> tag.
        response_data = render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
            
        })
        return HttpResponse(response_data)

    except:
        # If the month is not in the dictionary, return a 404 error with a custom message.
        return HttpResponseNotFound("<h1>Month is not supported :(</h1>")
