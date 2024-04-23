from django.contrib import admin
from .models import Category, UploadImage


class UploadImageAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Category)
admin.site.register(UploadImage, UploadImageAdmin)
