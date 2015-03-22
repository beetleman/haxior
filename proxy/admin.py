from django.contrib import admin
from models import Dane

# Register your models here.


class DaneAdmin(admin.ModelAdmin):
    list_display = ('url', 'type')
    list_filter = ('type', )
    search_fields = ('data', )

admin.site.register(Dane, DaneAdmin)
