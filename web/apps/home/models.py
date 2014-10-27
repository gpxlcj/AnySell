#! -*- coding:utf8 -*-
from django.db import models
from django.db.models import *
from system.user.models import BaseUser

class PurchaseCart(models.Model):

    '''
    购物车类
    '''

    user = OneToOneField(BaseUser, verbose_name=u'用户')

    class Meta:
        verbose_name = u'购物车'
        verbose_name_plural = u'购物车类'
        
    def __unicode__(self):
        return "%s" % user.name

class SellCart(models.Model):
   
    '''
    售货车类
    '''
    user = OneToOneField(BaseUser, verbose_name=u'用户')

    class Meta:
        verbose_name = u'售货车'
        verbose_name_plural = u'售货车类'
        
    def __unicode__(self):
        return '%s' % user.name
class Coordinate(models.Model):
  
    '''
    位置坐标类
    '''
    latitude = FloatField(verbose_name=u'纬度')
    longitude = FloatField(verbose_name=u'经度')

class District(models.Model):

    name = CharField(verbose_name=u'名称', max_length=30)

    class Meta:
        verbose_name = u'学部'
        verbose_name_plural = u'学部类'

    def __unicode__(self):
        return '%s' % self.name


class Dormintary(models.Model):
    '''
    宿舍类
    '''
    coordinate = OneToOneField(Coordinate, verbose_name=u'坐标类')
    name = CharField(verbose_name=u'名称', max_length=40)
    district = ForeignKey(District, verbose_name=u'学部')

    class Meta:
        verbose_name = u'宿舍'
        verbose_name_plural = u'宿舍类'

    def __unicode__(self):
        return '%s' % self.name


class Image(models.Model):
    '''
    插图类
    '''

    name = CharField(verbose_name=u'名称', max_length=100, blank=True)
    image = ImageField(verbose_name=u'图片地址', upload_to='img/')

    class Meta:
        verbose_name = u'图片'
        verbose_name_plural = u'图片类'

    def __unicode__(self):
        return '%s' % self.image


class Category(models.Model):
    '''
    类别类
    '''

    name = CharField(verbose_name=u'类别名')

    class Meta:
        verbose_name = u'类别'
        verbose_name_plural = u'类别类'

    def __unicode__(self):
        return '%s' % self.name


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

    class Meta:
        verbose_name = u'商品'
        verbose_name_plural = u'商品类'

    def __unicode__(self):
        return '%s' % self.title

