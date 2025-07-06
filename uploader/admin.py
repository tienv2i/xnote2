from django.contrib import admin
from . import models

@admin.register(models.UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'uploaded_at', 'uploaded_by')
    list_filter = ('uploaded_at', 'uploaded_by')
    search_fields = ('title', 'file')
    date_hierarchy = 'uploaded_at'
    ordering = ('-uploaded_at',)
    readonly_fields = ('uploaded_at',)

    def get_readonly_fields(self, request, obj=None):
        # Make 'uploaded_by' readonly if the file already exists
        if obj:
            return self.readonly_fields + ('uploaded_by',)
        return self.readonly_fields