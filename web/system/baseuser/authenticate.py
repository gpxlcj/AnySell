#! -*- coding:utf8 -*-

__author__ = 'gpxlcj'

from baseuser.models import BaseUser

USER_NOT_EXIST = {'status': 0}
USERNAME_BLANK = {'status': 1}
PASSWORD_WRONG = {'status': 2}

class LoginBackend(object):

    '''
    登陆后台管理
    '''
    def authenticate(self, username=None, password=None):

        if username:
            temp_str = username[-11:]
            if temp_str == '@whu.edu.cn':
                try:
                    user = BaseUser.objects.get(email=username)
                    if user.check_password(password):
                        return user
                    else:
                        return PASSWORD_WRONG
                except BaseUser.DoesNotExist:
                    return USER_NOT_EXIST
            else:
                try:
                    user = BaseUser.objects.get(username=username)
                    if user.check_password(passord):
                        return user
                    else:
                        return PASSWORD_WRONG
                except BaseUser.DoesNotExist:
                    return USER_NOT_EXIST
        else:
            return USERNAME_BLANK

    def get_user(self, user_id):

        try:
            return BaseUser.objects.get(pk=user_id)
        except BaseUser.DoesNotExist:
            return USER_NOT_EXIST