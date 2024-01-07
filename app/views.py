from __future__ import annotations

from typing import Union
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.request import Request
from .forms import UserRegisterForm, UserProfile, ProfileUpdateForm


def home(request):
    return redirect("app:login")


def register(request: Request) -> Union[render, redirect]:
    """
    This view handles both GET and POST requests for user registration. If the request is GET, it renders the
    registration form. If the request is POST, it validates the form and creates a new user. If the form is valid, it
    creates a new user, creates a token for the user, creates a user profile, and redirects the user to the login page.
    If the form is invalid, it renders the registration form again with the error message.
    """
    if request.method == "GET":
        context = {
            "form": UserRegisterForm(),
        }
        return render(request, "register.html", context)
    elif request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You are now able to log in")
            return redirect("app:login")
        else:
            context = {
                "form": form,
            }
            return render(request, "register.html", context)


@login_required
def profile(request: Request) -> render:
    """
    This view handles both GET and POST requests for user profile. If the request is GET, it renders the profile page.
    If the request is POST, it validates the form and updates the user profile. If the form is valid, it updates the
    user profile and redirects the user to the profile page. If the form is invalid, it renders the profile page again
    with the error message.
    """
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("app:profile")
    else:
        form = ProfileUpdateForm(instance=request.user)

    context = {"form": form, 'title': 'Profile'}
    return render(request, "profile.html", context)
