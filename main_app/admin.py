from django.contrib import admin
from .models import Book, Reader, Lib

# Register your models here.
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(Lib)