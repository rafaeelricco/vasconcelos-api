from django.contrib import admin
from products.models import Product
from images.models import Image
from products.models import Featured
from categories.models import Category, Family, SubFamily, ModelsAndVersions, SizeOfArea, Cultures, Disponibility, Launch


admin.site.register(Category)
admin.site.register(Family)
admin.site.register(SubFamily)
admin.site.register(ModelsAndVersions)
admin.site.register(SizeOfArea)
admin.site.register(Cultures)
admin.site.register(Disponibility)
admin.site.register(Launch)
admin.site.register(Featured)

admin.site.site_header = "Vasconcelos Agrícola"
admin.site.index_title = "Vasconcelos Agrícola | CMS"


class ImageInline(admin.TabularInline):
    model = Image
    extra = 8


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


class SlugExclude(admin.ModelAdmin):
    model = Product
    exclude = ('slug',)


admin.site.register(Product, ProductAdmin)
