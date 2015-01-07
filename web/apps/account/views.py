#! -*- coding:utf8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login, logout, authenticate, get_user_model

from lib.customjson import render_json

CustomUser = get_user_model()

def custom_register(request):

    '''
    用户注册
    '''

    if request.method == 'GET':
        return render_to_response('register.html', locals())
    elif request.method == 'POST':

        if request.POST.has_key('username'):
            username = request.POST['username']
        else:
            result = {'status': 10001}
            return render_json(result)

        #用户已经存在
        if CustomUser.objects.filter(username=username):
            result = {'status': 10006}
            return render_json(result)

        #邮箱为空
        if request.POST.has_key('email'):
            email = request.POST['email']
        else:
            result = {'status': 10007}
            return render_json(result)

        if CustomUser.objects.filter(email=email):
            result = {'status': 10008}
            return render_json(result)

        if request.POST.has_key('password'):
            password = request.POST['password']
        else:
            result = {'status': 0, 'error_code': 10002}
            return render_json(result)

        user = CustomUser.objects.create_user(email, username, password)
        return Http404
    else:
        return Http404

def custom_login(request):
    
    '''
    用户登陆
    '''

    if request.method == 'POST':

        #判断用户是否已经登陆
        if request.user.is_authenticated():
            result = {'status': 11002}
        #检验用户名是否为空
        try:
            username = request.POST['username']
        except:
            return render_json({'status': 0, 'error_code': 10001})
        if username=="" or username.isspace():
            return render_json({'status': 0, 'error_code': 10001})

        #检验密码是否为空
        try:
            password = request.POST['password']
        except:
            return render_json({'status': 10002})
        if password == "" or password.isspace():
            return render_json({'status': 10002})

        #检验用户名密码是否存在且正确
        user = authenticate(username=username, password=password)
        if user:
            #判断用户是否被激活
            if user.is_active:
                login(request, user)
                user.is_userlogin = True
                result = {'status': 11001}
                return render_json(result)
            else:
                result = {'status': 10005}
                return render_json(result)
        else:
            result = {'status': 10004}
            return render_json(result)

        return render_to_response('login.html', locals())

    elif request.method == 'GET':
        user = request.user
        if user.is_authenticated():
            user.is_userlogin = True
        return render_to_response('login.html', locals())

    else:
        return Http404

def custom_logout(request):
    
    '''
    用户登出
    '''

    if request.user.is_authenticated():
        username = request.user.username
        custom_user = CustomUser.objects.get(username=username)
        logout(request)
        custom_user.is_userlogin = False
        return redirect('/login/')
    else:
        return HttpResponse('<div>您已经登出了</div>')
