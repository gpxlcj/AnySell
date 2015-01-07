from django.contrib import admin
from apps.purchase.models import PurchaseCart, PurchaseComment 

class PurchaseCartAdmin(admin.ModelAdmin):

    list_display = ('user',)
    list_filter = ('user', )

class PurchaseCommentAdmin(admin.ModelAdmin):

    list_display = ('user', )

admin.site.register(PurchaseCart, PurchaseCartAdmin)
admin.site.register(PurchaseComment, PurchaseCommentAdmin)