from django.contrib import admin
from .models import project

# Register your models here.
class projectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(project,projectAdmin)
    