from django.contrib import admin

from kelas.models import *

# Register your models here.

class MapelAdmin(admin.ModelAdmin):
    list_display = ['kd_mapel','nama_mapel']
    list_filter = ('nama_mapel',)
    search_fields = ['nama_mapel']
    list_per_page = 25


admin.site.register(Mapel,MapelAdmin)

class KelasAdmin(admin.ModelAdmin):
    list_display = ['nama_kelas','jurusan']
    list_filter = ['jurusan']
    search_fields = []
    list_per_page = 25

admin.site.register(Kelas,KelasAdmin)

class AjarAdmin(admin.ModelAdmin):
    list_display = ['mapel','kd_guru','kelas']
    list_filter = ('mapel','kd_guru','kelas',)
    search_fields = ['mapel','kd_guru','kelas']
    list_per_page = 25

admin.site.register(Pengajar,AjarAdmin)