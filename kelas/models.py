from __future__ import unicode_literals

from guru.models import *
from django.db import models

# Create your models here.
class Kelas(models.Model):
    PILIH_NAMA_JURUSAN = (
        ('ipa','IPA'),
        ('ips','IPS'),
        ('bahasa','BAHASA'),
    )

    nama_kelas = models.CharField(max_length=10)
    jurusan = models.CharField(max_length=6, choices=PILIH_NAMA_JURUSAN)

    def __unicode__(self):
        return self.nama_kelas

class Mapel(models.Model):
    kd_mapel = models.CharField(max_length=10, primary_key=True)
    nama_mapel = models.CharField(max_length=10)

    def __unicode__(self):
        return self.nama_mapel

class Pengajar(models.Model):
    kd_guru = models.ForeignKey(Guru)
    mapel = models.ForeignKey(Mapel)
    kelas = models.ForeignKey(Kelas)

    def __unicode__(self):
        return self.mapel.nama_mapel
