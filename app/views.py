from __future__ import annotations
from typing import Union

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from rest_framework.request import Request

from .forms import UserRegisterForm, UserProfile, ProfileUpdateForm


# Lets structure it when are making a viewfirst handle the GET request and then the POST request
# Also when we are replying to a request instead of putting in dictionary made inside return redirect put a context
#


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
            user = form.save()

            # Create and associate a token with the user
            token, created = Token.objects.get_or_create(user=user)

            # Create UserProfile and associate it with the user
            UserProfile.objects.create(user=user)

            # form.cleaned_data.get('username')
            messages.success(request, "Your account has been created! You are now able to log in")
            return redirect("app:login")
        else:
            # error = form.errors.get() #Error is not comming exactly
            context = {
                "form": form,
                # 'error': error,
            }
            # form = UserRegisterForm()
            return render(request, "register.html", context)


@login_required
def profile(request: Request) -> render:
    """
    This view handles both GET and POST requests for user profile. If the request is GET, it renders the profile page.
    If the request is POST, it validates the form and updates the user profile. If the form is valid, it updates the
    user profile and redirects the user to the profile page. If the form is invalid, it renders the profile page again
    with the error message.
    """
    if request.method == "GET":
        user_profile = UserProfile.objects.get(user=request.user)
        context = {"profile": user_profile}
        return render(request, "profile.html", context)

    # if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm(request.POST,
    #                                request.FILES,
    #                                instance=request.user.profile)
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, f'Your account has been updated!')
    #         return redirect('app:profile')
    #
    # else:
    #     u_form = UserUpdateForm(instance=request.user)
    #     p_form = ProfileUpdateForm(instance=request.user.profile)
    #
    # context = {
    #     'u_form': u_form,
    #     'p_form': p_form
    # }

    # return render(request, 'profile.html', context)


def update_profile(request: Request) -> Union[render, redirect]:
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save()
            return redirect("profile")

    else:
        form = ProfileUpdateForm(instance=user_profile)

    context = {"form": form}
    return render(request, "update_profile.html", context)
