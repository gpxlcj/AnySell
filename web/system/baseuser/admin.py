#! -*-coding:utf8 -*-
from django.forms import ModelForm
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from baseuser.models import BaseUser


class BaseUserAdmin(UserAdmin):
    
    list_display = ('email', 'username','is_admin', 'is_active') 
    list_filter = ('is_admin', )
    search_fields = ('email', )
    ordering = ('is_admin', )

admin.site.register(BaseUser, BaseUserAdmin)
