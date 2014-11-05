#! -*- coding:utf8 -*-

from django.db import models
from system.baseuser import BaseUser

class SellCart(models.Model):

    '''
    售货车类
    '''
    user = models.OneToOneField(BaseUser, verbose_name=u'用户')

    class Meta:
        verbose_name = u'售货车'
        verbose_name_plural = u'售货车类'

    def __unicode__(self):
        return '%s' % user.name

class SellComment(models.Model):

    '''
    卖方被评价类
    '''
    user = models.OneToOneField(BaseUser, verbose_name=u'用户')

    class Meta:
        verbose_name = u'售货车'
        verbose_name_plural = u'售货车类'

    def __unicode__(self):
        return '%s' % user.name
