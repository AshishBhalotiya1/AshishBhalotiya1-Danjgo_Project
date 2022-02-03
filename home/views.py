from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.


def index(request):
    context = {
        "variable": "Ashish Bhalotiya"
    }
    return render(request, "index.html", context)
    # return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def mountain(request):
    return render(request, "mountain.html")


def beach(request):
    return render(request, "beach.html")


def desert(request):
    return render(request, "desert.html")


def Random(request):
    return render(request, "Random.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your details submited")
    return render(request, "contact.html")
