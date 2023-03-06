from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import information

class informationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...
# Register your models here.
admin.site.register(information,informationAdmin)