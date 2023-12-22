from django.contrib import admin
from used.images.models import Image
from used.models import Used


class ImageInline(admin.TabularInline):
    model = Image
    extra = 8


class UsedAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


class SlugExclude(admin.ModelAdmin):
    model = Used
    exclude = ('slug',)


admin.site.register(Used, UsedAdmin)
