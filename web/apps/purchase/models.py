#! -*- coding:utf8 -*-

from django.db import models
from django.contrib.auth import get_user_model
from system.customuser.models import CustomUser
from apps.home.models import Production

CustomUser = get_user_model()
class PurchaseCart(models.Model):

    '''
    购物车类
    '''

    user = models.OneToOneField(CustomUser, verbose_name=u'用户', related_name=u'purchase_cart')
    production = models.ManyToManyField(Production, verbose_name=u'车内物品', blank=True, related_name=u'purchase_production')

    class Meta:
        verbose_name = u'购物车'
        verbose_name_plural = u'购物车类'

    def __unicode__(self):
        return "%s" % self.user.username



class PurchaseComment(models.Model):

    '''
    买方评价类
    '''
    user = models.OneToOneField(CustomUser, verbose_name=u'用户', related_name=u'sellcomment')
    content = models.CharField(verbose_name=u'评价内容', max_length=400)

    class Meta:
        verbose_name = u'买方评价'
        verbose_name_plural = u'买方评价类'

    def __unicode__(self):
        return '%s' % self.user.username

