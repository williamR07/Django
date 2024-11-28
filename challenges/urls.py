from django.urls import path
from . import views


urlpatterns = [
    # The root URL that maps to the 'index' view
    path("", views.index, name="index"),
    # URL pattern that captures an integer 'month' parameter and maps it to the 'monthly_challenge_by_number' view
    path("<int:month>", views.monthly_challenge_by_number),
    # URL pattern that captures a string 'month' parameter and maps it to the 'monthly_challenge' view
    path("<str:month>", views.monthly_challenge, name="month-challenge")

]
