# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'get_enroll_number', 'is_staff', 'get_location')
    list_select_related = ('profile', )

    def get_location(self, instance):
        return instance.profile.role
    get_location.short_description = 'role'

    def get_enroll_number(self, instance):
        return instance.profile.enroll_number
    get_enroll_number.short_description = 'Enroll Number'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
