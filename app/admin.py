from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(AuthorModel)
admin.site.register(BookModel)