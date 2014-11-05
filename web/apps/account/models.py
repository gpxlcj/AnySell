#! -*- coding:utf8 -*-

from django.db import models
from system.baseuser.models import BaseUser

class DetailInfo(models.Model):

    name = models.CharField(verbose_name=u'姓名', blank=True)
    phone = models.CharField(verbose_name=u'手机号', blank=True)
    qq = models.CharField(verbose_name=u'qq号', blank=True)
    grade = models.CharField(verbose_name=u'年级', blank=True)
    college = models.CharField(verbose_name=u'学院', blank=True)

    user = models.OneToOneField(BaseUser, verbose_name=u'所属用户')

    dormintary = models.ForeignKey(BaseUser, verbose_name=u'宿舍', blank=True)

    class Meta:
        verbose_name = u'详细信息'
        verbose_name_plural = u'详细信息类'

    def __unicode__(self):
        return '%s' % user.name

class SellerInfo(models.Model):
    '''
    用户卖家信息
    '''

    credibility = models.IntegerField(verbose_name=u'信誉度', default=0)

    user = models.OneToOneField(BaseUser, verbose_name=u'所属用户')

    class Meta:
        verbose_name = u'用户卖家信息'
        verbose_name_plural = u'用户卖家信息类'

    def __unicode__(self):
        return "%s" %self.user.name

class CustomerInfo(models.Model):
    '''
    用户买家信息
    '''

    credibility = models.IntegerField(verbose_name=u'信誉度', default=0)

    user = models.OneToOneField(BaseUser, verbose_name=u'所属用户')

    class Meta:
        verbose_name = u'用户买家信息'
        verbose_name_plural = u'用户买家信息类'

    def __unicode__(self):
        return '%s'

