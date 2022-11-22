from django.contrib import admin
from parts.images.models import Image
from parts.models import Parts


class ImageInline(admin.TabularInline):
    model = Image
    extra = 8


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


class SlugExclude(admin.ModelAdmin):
    model = Parts
    exclude = ('slug',)


admin.site.register(Parts, ProductAdmin)
