from django.contrib import admin

from mainapp.models import Category, Hosting


class HostingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'prise',
        'disk',
        'site',
        'is_active',
    )


admin.site.register(Category)
admin.site.register(Hosting, HostingAdmin)
