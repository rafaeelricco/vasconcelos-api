from django.contrib import admin
from useds.images.models import Image
from useds.models import Useds


class ImageInline(admin.TabularInline):
    model = Image
    extra = 8


class UsedAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


class SlugExclude(admin.ModelAdmin):
    model = Useds
    exclude = ('slug',)


admin.site.register(Useds, UsedAdmin)
