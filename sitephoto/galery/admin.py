from django.contrib import admin
from django.db import models
from .models import *


class ItemAdmin(admin.ModelAdmin):
    fielsets = [
        (None, {'fields': ['title', 'slug', 'img', 'description']})
        ]
    list_display = ['title','slug']
    prepopulated_fields = {'slug':['title']}
    ordering = ['title']

class PhotoAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {"fields": ['title','item','img']})
        ]
    list_display = ['title','item','img']
    ordering = ['title']

    
class VideoAdmin(admin.ModelAdmin):

	fieldsets = [
		(None, {"fields":['title','video']})
		]
	list_display = ['title', 'video']
	ordering = ['title']
	

	
admin.site.register(Item, ItemAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Slider)

