#! -*- coding:utf8 -*-

from django.db import models
from system.customuser.models import CustomUser
from django.contrib.auth import get_user_model

CustomUser = get_user_model()
class DetailInfo(models.Model):

    name = models.CharField(verbose_name=u'姓名', blank=True, max_length=50)
    phone = models.CharField(verbose_name=u'手机号', blank=True, max_length=12)
    qq = models.CharField(verbose_name=u'qq号', blank=True, max_length=15)

    grade = models.CharField(verbose_name=u'年级', blank=True, max_length=20)
    college = models.CharField(verbose_name=u'学院', blank=True, max_length=40)

    user = models.OneToOneField(CustomUser, verbose_name=u'所属用户', related_name=u'user_detail_info' )

    dormintary = models.ForeignKey(CustomUser, verbose_name=u'宿舍', blank=True, related_name=u'detail_info')

    class Meta:
        verbose_name = u'详细信息'
        verbose_name_plural = u'详细信息类'

    def __unicode__(self):
        return '%s' % self.user.name

class SellerInfo(models.Model):
    '''
    用户卖家信息
    '''

    credibility = models.IntegerField(verbose_name=u'信誉度', default=0)

    user = models.OneToOneField(CustomUser, verbose_name=u'所属用户', related_name=u'sell_info')

    class Meta:
        verbose_name = u'用户卖家信息'
        verbose_name_plural = u'用户卖家信息类'

    def __unicode__(self):
        return "%s" % self.user.name

class CustomerInfo(models.Model):
    '''
    用户买家信息
    '''

    credibility = models.IntegerField(verbose_name=u'信誉度', default=0)

    user = models.OneToOneField(CustomUser, verbose_name=u'所属用户', related_name=u'customer_info')

    class Meta:
        verbose_name = u'用户买家信息'
        verbose_name_plural = u'用户买家信息类'

    def __unicode__(self):
        return '%s' % self.user.name

