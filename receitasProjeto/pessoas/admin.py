from django.contrib import admin
from .models import Person


# Register your models here.

class listPerson(admin.ModelAdmin):
    list_display = ('id', 'person_name', 'person_email')
    list_display_links = ('id', 'person_name')
    search_fields = ('person_name',)
    list_per_page = 5


admin.site.register(Person, listPerson)
