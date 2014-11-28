#! -*- coding:utf8 -*-

from django.db import models
from django.db.models import *
from django.contrib.auth import get_user_model

from system.customuser.models import CustomUser
from apps.sell.models import SellCart, SellComment
from apps.purchase.models import PurchaseCart, PurchaseComment
from apps.base.models import Image, Coordinate

CustomUser = get_user_model()


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
    name = models.CharField(verbose_name=u'类别名', max_length=30)

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
    title = CharField(verbose_name=u'标题', max_length=120)
    description = CharField(verbose_name=u'描述', max_length=500)
    price = FloatField(verbose_name=u'价格')
    number = IntegerField(verbose_name=u'数量', default=-1)
    images = ManyToManyField(Image, verbose_name=u'插图')
    category = ForeignKey(Category, verbose_name=u'类别', related_name=u'production_category')
    sell_cart = ForeignKey(SellCart, verbose_name=u'售货车')
    purchase_cart = ForeignKey(PurchaseCart, verbose_name=u'购物车')
    status = CharField(choices=PRO_STATUS, verbose_name=u'状态', max_length=10)


    class Meta:
        verbose_name = u'商品'
        verbose_name_plural = u'商品类'

    def __unicode__(self):
        return '%s' % self.title


class Comment(models.Model):
    '''
    评论类
    '''
    user = models.ForeignKey(CustomUser, verbose_name=u'评价者', related_name=u'give_comment')
    obj_user = models.ForeignKey(CustomUser, verbose_name=u'被评价者', related_name=u'given_comment')

    class Meta:
        verbose_name = u'评论'
        verbose_name = u'商品类'

    def __unicode__(self):
        return '%s' % self.obj_user.name

