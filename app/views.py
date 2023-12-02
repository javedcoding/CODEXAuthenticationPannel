from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserProfile, ProfileUpdateForm

# Lets structure it when are making a viewfirst handle the GET request and then the POST request
# Also when we are replying to a request instead of putting in dictionary made inside return redirect put a context
#

def home(request):
    return redirect('app:login')


def register(request):
    if request.method == 'GET':
        context = {
            'form': UserRegisterForm(),
        }
        return render(request, 'register.html', context)
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('app:login')
        else:
            # error = form.errors.get() #Error is not comming exactly
            context = {
                'form': UserRegisterForm(),
                # 'error': error,
            }
            # form = UserRegisterForm()
            return render(request, 'register.html', context)


@login_required
def profile(request):
    '''
    '''
    if request.method == 'GET':
        user_profile = UserProfile.objects.get(user=request.user)
        context = {
            'profile': user_profile
        }
        return render(request, 'profile.html', context)

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

def update_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=user_profile)

    context = {
        'form': form
    }
    return render(request, 'update_profile.html', context)
