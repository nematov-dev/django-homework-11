from django.contrib import admin

from . import models

admin.site.register(models.ContactModel)

@admin.register(models.AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'job')  # Admin panelda ko'rsatiladigan ustunlar
    search_fields = ('name', 'job')  # Qidiruv maydonchalari
    list_filter = ('job',)  # Filtr uchun maydon

