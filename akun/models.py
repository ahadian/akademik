from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from siswa import models as siswa
from guru import models as guru

# Create your models here.

class AkunSiswa (models.Model):
    PILIH_JENIS_AKUN = (
        ('siswa','Siswa'),
        ('admin','Administrator'),
    )
    akun = models.ForeignKey(User)
    siswa = models.ForeignKey(siswa.Siswa)
    jenis_akun = models.CharField(max_length=20, choices=PILIH_JENIS_AKUN)

    def __unicode__(self):
        return self.siswa.nama


class AkunGuru (models.Model):
    PILIH_JENIS_AKUN = (
        ('guru','Guru'),
        ('admin','Administrator'),
    )
    akun = models.ForeignKey(User)
    guru = models.ForeignKey(guru.Guru)
    jenis_akun = models.CharField(max_length=20, choices=PILIH_JENIS_AKUN)

    def __unicode__(self):
        return self.guru.nama
