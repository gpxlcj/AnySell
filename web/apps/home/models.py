#! -*- coding:utf8 -*-
from django.db import models
from account.models import SellUser

class BuyCart(models.Model):

    user = OneToOneField(SellUser, verbose_name=u'用户')

    class Meta:
        verbose_name = u'购物车'
        verbose_name_plural = u'购物车类'
        
    def __unicode__(self):
        return "%s" %user.name

class SellCart(models.Model):
   
    '''
    售货车类
    '''
    user = OneToOneField(SellUser, verbose_name=u'用户')

    class Meta:
        verbose_name = u'售货车'
        verbose_name_plural = u'售货车类'
        
    def __unicode__(self):
        return '%s' %user.name
class Coordinate(models.Model):
  
    '''
    位置坐标类
    '''
    latitude = FloatField(verbose_name=u'纬度', )
    longitude = FloatField(verbose_name=u'经度', )

class District(models.Model):

    name = CharField(verbose_name=u'名称', )

class Dormintary(models.Model):

    coordinate = OneToOneField(verbose_name=u'坐标类', )
    name = CharField(verbose_name=u'名称', )
    district = ForeignKey(verbose_name=u'学部', )



class Detail_info(models.Model):

    name = StringField(verbose_name=u'姓名', blank=True)
    phone = StringField(verbose_name=u'手机号', blank=True)
    qq = StringField(verbose_name=u'qq号', blank=True)
    grade = StringField(verbose_name=u'年级', blank=True)
    college = StringField(verbose_name=u'学院', blank=True)
    
    user = OneToOneField(SellUser, verbose_name=u'用户')

    dormintary = ForeignKey(SellUser, verbose_name=u'宿舍', blank=True)

    class Meta:
        verbose_name = u'详细信息'
        verbose_naem_plural = u'详细信息类'

    def __unicode__(self):
        return '%s' %user.name

  
    
