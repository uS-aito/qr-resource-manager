from django.contrib import admin

from .models import Book, Monitor

# Register your models here.
# admin.site.register(Resource)
admin.site.register(Book)
admin.site.register(Monitor)