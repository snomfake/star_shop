from django.contrib import admin

from shop.models import Client, Categorie, Star, Review


class ReviewInline(admin.StackedInline):
    """"""
    model = Review
    extra = 1


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """"""
    pass


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    """"""
    pass


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    """"""
    list_display = ('name', 'slug', 'price', 'is_active')
    list_filter = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
    ordering = ('is_active', 'created_at', 'updated_at')
    inlines = (ReviewInline,)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """"""
    pass

