# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView

from accounts.models import Profile
from result.models import Marksheet

# Create your views here.


@login_required
def marksheet_list(request):
    profile = Profile.objects.filter(user_id=request.user.id).first()
    marksheets = Marksheet.objects.filter(student_name=profile)
    return render(request, 'result/marksheet_list.html', {'marksheets': marksheets})


class MarksheetDetailView(LoginRequiredMixin, DetailView):
    model = Marksheet
