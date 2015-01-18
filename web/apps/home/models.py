#! -*- coding:utf8 -*-

from django.db import models
from django.contrib.auth import get_user_model

from system.customuser.models import CustomUser
from apps.base.models import Image, Coordinate

CustomUser = get_user_model()


class District(models.Model):

    '''
    学部类
    '''

    name = models.CharField(verbose_name=u'名称', max_length=30)
    id_code = models.PositiveIntegerField(verbose_name=u'编号', unique=True)

    class Meta:
        verbose_name = u'学部'
        verbose_name_plural = u'学部类'

    def __unicode__(self):
        return '%s' % self.name


class Dormitory(models.Model):

    '''
    宿舍类
    '''

    coordinate = models.OneToOneField(Coordinate, verbose_name=u'坐标类')
    name = models.CharField(verbose_name=u'名称', max_length=40)
    district = models.ForeignKey(District, verbose_name=u'学部')
    id_code = models.PositiveIntegerField(verbose_name=u'编号', unique=True)

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
    ('1', u'已预订'),
    ('2', u'在售'),
    ('3', u'下架'),
)


class Label(models.Model):

    '''
    标签名
    '''

    name = models.CharField(verbose_name=u'标签名', max_length=200, unique=True)

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = u'标签名'

    def __unicode__(self):
        return "%s" % self.name


class Production(models.Model):

    '''
    商品类
    '''

    title = models.CharField(verbose_name=u'标题', max_length=120)
    description = models.CharField(verbose_name=u'描述', max_length=600)
    price = models.FloatField(verbose_name=u'价格')
    number = models.IntegerField(verbose_name=u'数量', default=-1)
    images = models.ManyToManyField(Image, verbose_name=u'插图', related_name=u'production_images')
    cover = models.OneToOneField(Image, verbose_name=u'封面', blank=True, related_name=u'production_cover')

    publish_time = models.DateTimeField(verbose_name=u'发布时间', auto_now=True)
    hit_num = models.IntegerField(verbose_name=u'点击数', default=0)

    category = models.ForeignKey(Category, verbose_name=u'类别', related_name=u'production_category')
    label = models.ManyToManyField(Label, verbose_name=u'标签', related_name=u'production_label')


    status = models.CharField(choices=PRO_STATUS, verbose_name=u'状态', max_length=10)


    class Meta:
        verbose_name = u'商品'
        verbose_name_plural = u'商品类'

    def __unicode__(self):
        return '%s' % self.title


class Comment(models.Model):
    '''
    评论类
    '''
    title = models.CharField(verbose_name=u'标题', max_length=200, blank=True)
    content = models.CharField(verbose_name=u'内容', max_length=500)
    time = models.DateTimeField(verbose_name=u'时间', auto_now=True)
    user = models.ForeignKey(CustomUser, verbose_name=u'评价者', related_name=u'give_comment')
    obj_user = models.ForeignKey(CustomUser, verbose_name=u'被评价者', related_name=u'given_comment')

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论类'

    def __unicode__(self):
        return '%s' % self.obj_user.name

