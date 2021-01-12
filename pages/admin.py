from django.contrib import admin
from .models import  Messages, Lessons , Texts

# Register your models here.

admin.site.register(Texts)
admin.site.register(Messages)
admin.site.register(Lessons)
