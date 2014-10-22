from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from admin import PassportManager

# Create your models here.

class SellUser(AbstactBaseUser)
    '''
    用户类
    '''
    email = models.EmailField(verbose_name=u'邮箱')
    username = models.CharField(verbose_name=u'用户名', max_length=30)
    password = models.CharField(verbose_name=u'密码',max_length=30)
    auth_key = models.CharField(verbose_name=u'验证码', max_length = 200)
    update_key = models.CharField(verbose_name=u'更新验证码', max_length = 200)
    is_activate = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','email','password']

    objects = PassportManager()

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户类'


