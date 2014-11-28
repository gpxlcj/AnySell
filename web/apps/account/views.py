#! -*- coding:utf8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404

def test(request):
    
    if request.method == 'POST':
        password =request.POST.get('password')
        email = request.POST.get('email')

        render_to_response('test.html', locals())

    elif request.method == 'GET':
        render_to_response('test.html', locals())

    else:
        return Http404
