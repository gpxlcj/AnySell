#! -*- coding:utf8 -*-

from django.contrib import admin
from apps.home.models import District, Dormitory, Category, Production, Comment


class DistrictAdmin(admin.ModelAdmin):
    
    list_display = ('name',)

class DormitoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'district', 'coordinate', )

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', )

class ProdutionAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'price', 'number', 'category', 'status', 'publish_time')

class CommentAdmin(admin.ModelAdmin):

    list_display = ('user', 'obj_user', 'content', 'time', 'title', )






admin.site.register(District, DistrictAdmin)
admin.site.register(Dormitory, DormitoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Production, ProdutionAdmin)
admin.site.register(Comment, CommentAdmin)