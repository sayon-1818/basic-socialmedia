from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    user = request.user
    hello = "hello"

    context = {
        "user":user,
        # "hello":hello,
    }

    return render(request, "main/home.html", context)