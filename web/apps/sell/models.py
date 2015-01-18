#! -*- coding:utf8 -*-

from django.db import models
from django.contrib.auth import get_user_model
from system.customuser.models import CustomUser
from apps.home.models import Production

CustomUser = get_user_model()

class SellCart(models.Model):

    '''
    售货车类
    '''
    user = models.OneToOneField(CustomUser, verbose_name=u'用户', related_name=u'sell_cart')
    production = models.ManyToManyField(Production, verbose_name=u'车内物品', blank=True, related_name=u'sell_production')


    class Meta:
        verbose_name = u'售货车'
        verbose_name_plural = u'售货车类'

    def __unicode__(self):
        return '%s' % self.user.username

class SellComment(models.Model):

    '''
    卖方被评价类
    '''
    user = models.OneToOneField(CustomUser, verbose_name=u'用户', related_name=u'sell_comment')

    class Meta:
        verbose_name = u'卖方被评价'
        verbose_name_plural = u'卖方被评价类'

    def __unicode__(self):
        return '%s' % self.user.username
