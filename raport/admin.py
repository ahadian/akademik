from django.contrib import admin

from raport.models import *

# Register your models here.

class RaportSiswa(admin.ModelAdmin):
    list_display = ['id_siswa','id_mapel','id_guru','id_kelas','tahun_ajaran','harian','uts','uas']
    list_filter = ('id_mapel','id_kelas','semester','tahun_ajaran','id_siswa',)
    search_fields = ['id_siswa',]
    list_per_page = 30

admin.site.register(Raport,RaportSiswa)