from django.contrib import admin

# Register your models here.
from processing.models import IndexWord, Posting

admin.site.register(IndexWord)
admin.site.register(Posting)
