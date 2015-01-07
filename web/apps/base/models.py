#! -*- coding:utf8 -*-

from django.db import models


class Image(models.Model):
    '''
    插图类
    '''

    name = models.CharField(verbose_name=u'名称', max_length=100, blank=True)
    image = models.ImageField(verbose_name=u'图片地址', upload_to='img/')
    date = models.DateTimeField(verbose_name=u'上传时间', auto_now = True)

    class Meta:
        verbose_name = u'图片'
        verbose_name_plural = u'图片类'

    def __unicode__(self):
        return '%s' % self.name



class Coordinate(models.Model):
  
    '''
    位置坐标类
    '''
    latitude = models.FloatField(verbose_name=u'纬度')
    longitude = models.FloatField(verbose_name=u'经度')

    class Meta:
        verbose_name = u'坐标'
        verbose_name_plural = u'坐标类'

    def __unicode__(self):
        return '%s' % self.id
