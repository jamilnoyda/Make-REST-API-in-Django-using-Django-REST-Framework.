# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    """
    Profie model for user which uses Django's User model
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')

    STUDENT = 'Student'
    TEACHER = 'Teacher'
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    )
    role = models.CharField(
        choices=ROLE_CHOICES, null=True, blank=True, max_length=10, help_text='Role')
    enroll_number = models.PositiveIntegerField(null=True, unique=True, help_text='Enroll Number')

    def __unicode__(self):
        return self.user.username

    class Meta:
        def __unicode__(self):
            return self.title
