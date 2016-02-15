from django.contrib import admin
from .models import Osoba, Oceny, Wpisy

# Register your models here.

class OcenyInline(admin.TabularInline):
    model = Oceny

class OsobaAdmin(admin.ModelAdmin):
    inlines = [OcenyInline]
    

admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Wpisy)
