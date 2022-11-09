from django.contrib import admin
from catalog.models import catalog_item, catalog_category, catalog_tag


class catalog_item_admin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_published",
        'img_tmb',
    )
    list_editable = ("is_published",)
    list_display_links = ("name",)
    filter_horizontal = ("tags",)


admin.site.register(catalog_item, catalog_item_admin)
admin.site.register(catalog_category)
admin.site.register(catalog_tag)
