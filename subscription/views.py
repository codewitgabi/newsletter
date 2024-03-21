from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
# from django.urls import reverse
from django.views.generic import CreateView
from django.contrib import messages

from .models import Subscriber


class IndexView(CreateView):
    template_name = "subscription/index.html"
    model = Subscriber
    fields = ["email"]

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        _, created = Subscriber.objects.get_or_create(
            email=request.POST.get("email"))

        if not created:
            print("Error message")
            messages.error(request, "You are already subscribed.")

        return redirect("index")
