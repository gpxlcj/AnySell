from django.contrib import admin
from apps.sell.models import SellCart, SellComment

class SellCartAdmin(admin.ModelAdmin):

    list_display = ('user', )

class SellCommentAdmin(admin.ModelAdmin):

    list_display = ('user', )

admin.site.register(SellCart, SellCartAdmin)
admin.site.register(SellComment, SellCommentAdmin)