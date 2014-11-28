#! -*- coding:utf8 -*-

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.conf import settings

class PassportManager(BaseUserManager):
   
    '''
    账户管理
    '''
    #创建账户
    def create_user(self, email, username, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = PassportManager.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    #创建超级账户
    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username=username, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_activate = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    '''
    用户类
    '''
    email = models.EmailField(verbose_name=u'邮箱', unique=True, db_index=True)
    username = models.CharField(verbose_name=u'用户名', max_length=30)
    auth_key = models.CharField(verbose_name=u'验证身份码', max_length=200)
    update_key = models.CharField(verbose_name=u'更新验证身份码', max_length=200)
    is_activate = models.BooleanField(verbose_name=u'是否激活', default=False)
    is_active = models.BooleanField(verbose_name=u'是否登陆', default=False)
    is_staff = models.BooleanField(verbose_name=u'是否管理员', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = PassportManager()

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户类'
        app_label = 'customuser'

    def get_full_name(self):
        return '%s' %self.username

    def get_short_name(self):
        return '%s' %self.username
    
    def has_module_perms(self, app_label):
        return True

    def has_perms(perm_list, obj=None):
        return True

    def has_perm(perm, obj=None):
        return True

