#! -*- coding:utf8 -*-

from django.contrib.auth.models import AbstractBaseUser

from django.db import models
from manage import PassportManager

class BaseUser(AbstractBaseUser):
    '''
    用户类
    '''
    email = models.EmailField(verbose_name=u'邮箱')
    username = models.CharField(verbose_name=u'用户名', max_length=30)
#    password = models.CharField(verbose_name=u'密码', max_length=30)
    auth_key = models.CharField(verbose_name=u'验证身份码', max_length = 200)
    update_key = models.CharField(verbose_name=u'更新验证身份码', max_length = 200)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email']

    objects = PassportManager()

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户类'
        app_label = 'user'


