from django.contrib import admin

from .models import KeyValue
# Register your models here.
@admin.register(KeyValue)
class KeyValueAdmin(admin.ModelAdmin):
    list_display = ("key" , "value" , "created_at" , "updated_at")
    search_fields = ("key" , "value")