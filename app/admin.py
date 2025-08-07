from django.contrib import admin
from .models import *
# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    
admin.site.register(Hospital),
admin.site.register(Form),  
admin.site.register(Form1),  
admin.site.register(FileDoc),  
admin.site.register(FileDoc1),  