#! -*- coding:utf8 -*-

from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class PassportManager(BaseUserManager):

    #创建账户
    def _create_user(self, email, username, password=None):
        
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
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user
