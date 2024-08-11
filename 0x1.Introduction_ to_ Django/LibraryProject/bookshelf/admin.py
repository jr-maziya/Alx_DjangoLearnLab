from .models import Book
from django.contrib import admin
admin.site.register(Book)
"register", "admin.ModelAdmin"
"list_filter", "author", "publication_year"

# Register your models here.
