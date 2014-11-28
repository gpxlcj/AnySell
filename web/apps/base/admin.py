from django.contrib import admin
from models import Image, Coordinate

class ImageAdmin(admin.ModelAdmin):

    list_display = ('name', 'image', 'date')
    search_fields = ('date', )
    date_hierarchy = 'date'
    ordering = ('-date', )

class CoordinateAdmin(admin.ModelAdmin):

    list_display = ('latitude', 'longitude')
    search_fields = ('latitude', 'longitude') 
   
admin.site.register(Image, ImageAdmin)
admin.site.register(Coordinate, CoordinateAdmin)




