#! -*- coding:utf8 -*-

__author__ = 'gpxlcj'

import re
from system.customuser.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginBackend(object):

    def authenticate(self, username=None, password=None):

        if username:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", username)!=None:
                try:
                    user = User.objects.get(email = username)
                    if user.check_password(password):
                        return user
                    return None
                except User.DoesNotExist:
                    return None

            elif len(username)==11 and re.match("^(1[3456]\d{9})$", username)!=None:
                try:
                    user = User.objects.get(usermobile = username)
                    if user.check_password(password):
                        return user
                    return None
                except User.DoseNotExist:
                    return None

            else:
                try:
                    user = User.objects.get(username = username)
                    if user.check_password(password):
                        return user
                    return None
                except User.DoesNotExist:
                    return None
        else:
            return None

    def get_user(self, user_id):

        try:
            return User.objects.get(pk = user_id)
        except User.DoesNotExist:
            return None




