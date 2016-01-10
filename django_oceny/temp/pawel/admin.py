from django.contrib import admin
from .models import Osoba, Oceny

# Register your models here.

class OcenyInline(admin.TabularInline):
    model = Oceny

class OsobaAdmin(admin.ModelAdmin):
    inlines = [OcenyInline]
    

admin.site.register(Osoba, OsobaAdmin)
