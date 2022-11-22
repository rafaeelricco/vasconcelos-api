from django.contrib import admin
from products.models import Product
from products.images.models import Image
from categories.models import (
    Category,
    Family,
    SubFamily,
    ModelsAndVersions,
    SizeOfArea,
    Cultures,
    Disponibility,
    Launch,
)
from text_block.models import TextBlock

admin.site.site_header = "Vasconcelos Agrícola"
admin.site.index_title = "Vasconcelos Agrícola | CMS"

admin.site.register(Category)
admin.site.register(Family)
admin.site.register(SubFamily)
admin.site.register(ModelsAndVersions)
admin.site.register(SizeOfArea)
admin.site.register(Cultures)
admin.site.register(Disponibility)
admin.site.register(Launch)


class TextBlockInline(admin.StackedInline):
    model = TextBlock
    extra = 1


class ImageInline(admin.StackedInline):
    model = Image
    extra = 8


class ProductAdmin(admin.ModelAdmin):
    inlines = [TextBlockInline, ImageInline]


class SlugExclude(admin.ModelAdmin):
    model = Product
    exclude = ("slug",)


admin.site.register(Product, ProductAdmin)
