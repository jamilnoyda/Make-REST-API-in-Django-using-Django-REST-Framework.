# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from forms import SendPDFForm, SignUpForm, ProfileForm, StandardForm
from result.models import Marksheet

# Create your views here.


def standard(request):

    if request.user.is_staff:
        if request.method == 'POST':

            form = StandardForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Standard Successfully added ')

                return redirect('/teachers/standard/')
            else:
                messages.success(request, 'Invalid !')
                return redirect('/teachers/standard/')
        else:
            form = StandardForm()
            return render(request, 'teachers/teachers.html', {
                'form': form, })
    else:
        return redirect(settings.LOGIN_REDIRECT_URL)


class MarksheetDetailView(LoginRequiredMixin, DetailView):
    model = Marksheet


class MarksheetListView(LoginRequiredMixin, ListView):
    model = Marksheet
    context_object_name = 'marksheets'


@login_required
def home(request):
    if request.user.is_staff:
        if request.method == 'POST':

            form = SendPDFForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(request)
                return redirect('/teachers')
            else:
                messages.success(request, 'Invalid File Format!')
                return redirect('/teachers')
        else:
            form = SendPDFForm()
            return render(request, 'teachers/teachers.html', {
                'form': form, })
    else:
        return redirect(settings.LOGIN_REDIRECT_URL)


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
