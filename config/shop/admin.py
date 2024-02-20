from django.contrib import admin

from shop.models import Client, Categorie, Star, Review


class ReviewInline(admin.StackedInline):
    """Adding `Review` model to `Star` model in inline mode"""

    model = Review
    extra = 1


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Registration of `Client` model in admin panel"""

    pass


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    """Registration of `Categorie` model in admin panel"""

    pass


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    """Registration of `Star` model in admin panel"""

    list_display = ("name", "slug", "price", "is_active")
    list_filter = ("created_at", "updated_at")
    prepopulated_fields = {"slug": ("name",)}
    date_hierarchy = "created_at"
    ordering = ("is_active", "created_at", "updated_at")
    inlines = (ReviewInline,)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Registration of `Review` model in admin panel"""

    pass


# change admin panel title
admin.site.set_title = "Star Shop 🏬🌠"
admin.site.site_header = "Star Shop 🏬🌠"
