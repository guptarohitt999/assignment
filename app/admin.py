from django.contrib import admin
from app.models import Upload

# Register your models here.

class UploadAdmin(admin.ModelAdmin):
    list_display=('profile','doc')

admin.site.register(Upload,UploadAdmin)
