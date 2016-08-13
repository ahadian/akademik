from django.contrib import admin
from guru.models import *

# Register your models here.

class GuruAdmin(admin.ModelAdmin):
    list_display = ['nip','nama','alamat','tgl_lahir','telepon','email']
    list_filter = ()
    search_fields = ['nip','nama','telepon','email']
    list_per_page = 25

admin.site.register(Guru,GuruAdmin)

