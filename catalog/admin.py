from django.contrib import admin

from catalog.models import (catalog_category, catalog_item,
                            catalog_item_gallery, catalog_item_preview,
                            catalog_tag)


class catalog_item_admin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_published",
        "is_on_main"
    )
    list_editable = ("is_published", "is_on_main",)
    list_display_links = ("name",)
    filter_horizontal = ("tags",)


class catalog_item_image_admin(admin.ModelAdmin):
    list_display = (
        'img_tmb',
    )


admin.site.register(catalog_item, catalog_item_admin)
admin.site.register(catalog_category)
admin.site.register(catalog_tag)
admin.site.register(catalog_item_preview, catalog_item_image_admin)
admin.site.register(catalog_item_gallery, catalog_item_image_admin)
