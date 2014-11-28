# !-*- coding:utf8 -*-
from django.contrib import admin
from apps.account.models import DetailInfo, SellerInfo, CustomerInfo 

class DetailInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'qq', 'grade', 'college', 'user', 'dormintary')


class SellerInfoAdmin(admin.ModelAdmin):
    '''
    卖方信息类
    '''
    list_display = ('credibility', 'user',)

class CustomerInfoAdmin(admin.ModelAdmin):
    '''
    买方信息类
    '''
    list_display = ('credibility', 'user',)

admin.site.register(DetailInfo, DetailInfoAdmin) 
admin.site.register(SellerInfo, SellerInfoAdmin) 
admin.site.register(CustomerInfo, CustomerInfoAdmin) 
