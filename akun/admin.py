from django.contrib import admin
from akun.models import *

# Register your models here.
class AkunSiswaAdmin (admin.ModelAdmin):
    list_display = ['akun','jenis_akun','siswa']
    list_filter = ('jenis_akun',)
    search_fields = []
    list_per_page = 25

admin.site.register(AkunSiswa,AkunSiswaAdmin)

class AkunGuruAdmin (admin.ModelAdmin):
    list_display = ['akun', 'jenis_akun', 'guru']
    list_filter = ('jenis_akun',)
    search_fields = []
    list_per_page = 25

admin.site.register(AkunGuru, AkunGuruAdmin)