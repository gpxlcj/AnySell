#! -*- coding:utf8 -*-

from django.db import models
from django.contrib.auth import get_user_model
from system.customuser.models import CustomUser

CustomUser = get_user_model()
class PurchaseCart(models.Model):

    '''
    购物车类
    '''

    user = models.OneToOneField(CustomUser, verbose_name=u'用户', related_name=u'purchase_cart')

    class Meta:
        verbose_name = u'购物车'
        verbose_name_plural = u'购物车类'

    def __unicode__(self):
        return "%s" % self.user.name



class PurchaseComment(models.Model):

    '''
    买方评价类
    '''
    user = models.OneToOneField(CustomUser, verbose_name=u'用户', related_name=u'sellcomment')

    class Meta:
        verbose_name = u'售货车'
        verbose_name_plural = u'售货车类'

    def __unicode__(self):
        return '%s' % self.user.name

