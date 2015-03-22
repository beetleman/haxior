from django.contrib import admin
from models import Dane

# Register your models here.


class DaneAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dane, DaneAdmin)
