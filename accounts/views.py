# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from forms import SignUpForm, ProfileForm

# Create your views here.


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            profile_form = ProfileForm(request.POST)

            if form.is_valid() and profile_form.is_valid():
                form.save()
                user_name = form.cleaned_data['username']
                profile_form.save(user_name)
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/accounts')
        else:
            form = SignUpForm()
            profile_form = ProfileForm()

        return render(request, 'accounts/signup.html', {'form': form, 'profile_form': profile_form})
    else:
        return redirect('/accounts')


@login_required
def profile(request):
    return render(request, "accounts/profile.html")
