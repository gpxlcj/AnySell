from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.contrib.auth import login, logout, get_user_model

custom_user = get_user_model()

def custom_login(request):
    pass

def custom_logout(request):
    pass

def custom_register(request):
    pass