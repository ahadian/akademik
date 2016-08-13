from django.contrib import admin
from siswa.models import *

# Register your models here.

class SiswaAdmin (admin.ModelAdmin):
    list_display = ['nis','nama','alamat','tgl_lahir','tahun_masuk','jurusan','kelas_sekarang']
    list_filter = ('tahun_masuk','jurusan','kelas_sekarang')
    search_fields = ['nama','alamat','tgl_lahir']
    list_per_page = 25

admin.site.register(Siswa,SiswaAdmin)

