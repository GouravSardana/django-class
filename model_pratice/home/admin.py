from django.contrib import admin

# Register your models here
from import_export.admin import ImportExportModelAdmin

from home.models import Medical_library

@admin.register(Medical_library)
class Medical_libraryAdmin(ImportExportModelAdmin):
    pass