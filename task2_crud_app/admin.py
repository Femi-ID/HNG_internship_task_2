from django.contrib import admin
from .models import Person
# Register your models here.


@admin.register(Person)
class Person(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('created',)
    search_fields = ['last_name']
