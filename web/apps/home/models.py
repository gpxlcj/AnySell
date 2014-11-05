#! -*- coding:utf8 -*-

from django.db import models
from django.db.models import *
from basesystem.user.models import BaseUser
from sell.models import SellCart, SellComment
from purchase.models import PurchaseCart, PurchaseComment
from base.models import Image, Coordinate


class District(models.Model):

    '''
    学部类
    '''
    name = models.CharField(verbose_name=u'名称', max_length=30)

    class Meta:
        verbose_name = u'学部'
        verbose_name_plural = u'学部类'

    def __unicode__(self):
        return '%s' % self.name


class Dormintary(models.Model):

    '''
    宿舍类
    '''
    coordinate = models.OneToOneField(Coordinate, verbose_name=u'坐标类')
    name = models.CharField(verbose_name=u'名称', max_length=40)
    district = models.ForeignKey(District, verbose_name=u'学部')

    class Meta:
        verbose_name = u'宿舍'
        verbose_name_plural = u'宿舍类'

    def __unicode__(self):
        return '%s' % self.name


class Category(models.Model):

    '''
    类别类
    '''
    name = models.CharField(verbose_name=u'类别名')

    class Meta:
        verbose_name = u'类别'
        verbose_name_plural = u'类别类'

    def __unicode__(self):
        return '%s' % self.name

PRO_STATUS = (
    (1, u'已预订'),
    (2, u'在售'),
)

class Production(models.Model):

    '''
    商品类
    '''
    title = CharField(verbose_name=u'标题')
    description = CharField(verbose_name=u'描述')
    price = FloatField(verbose_name=u'价格')
    number = IntegerField(verbose_name=u'数量', default=-1)
    images = ManyToManyField(Image, verbose_name=u'插图')
    category = ForeignKey(Category, verbose_name=u'类别')
    sell_cart = ForeignKey(SellCart, verbose_name=u'售货车')
    purchase_cart = ForeignKey(PurchaseCart, verbose_name=u'购物车')
    status = CharField(choices = PRO_STATUS, verbose_name=u'状态', max_length=10)


    class Meta:
        verbose_name = u'商品'
        verbose_name_plural = u'商品类'

    def __unicode__(self):
        return '%s' % self.title


class Comment(models.Model):
    '''
    评论类
    '''
    user = models.ForeignKey(BaseUser, verbose_name=u'评价者')
    obj_user = models.ForeignKey(BaseUser, verbose_name=u'被评价者')

    class Meta:
        verbose_name = u'评论'
        verbose_name = u'商品类'

    def __unicode__(self):
        return '%s' % self.obj_user.name

