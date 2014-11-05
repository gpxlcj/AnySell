#! -*- coding:utf8 -*-

from django.db import models
from system.user.models import BaseUser

class PurchaseCart(models.Model):

    '''
    购物车类
    '''

    user = models.OneToOneField(BaseUser, verbose_name=u'用户')

    class Meta:
        verbose_name = u'购物车'
        verbose_name_plural = u'购物车类'

    def __unicode__(self):
        return "%s" % user.name



class SellComment(models.Model):

    '''
    买方评价类
    '''
    user = models.OneToOneField(BaseUser, verbose_name=u'用户')

    class Meta:
        verbose_name = u'售货车'
        verbose_name_plural = u'售货车类'

    def __unicode__(self):
        return '%s' % user.name
