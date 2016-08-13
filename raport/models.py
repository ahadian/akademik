from __future__ import unicode_literals

from django.db import models


from siswa.models import *
from kelas.models import *

# Create your models here.

class Raport(models.Model):
    id_siswa = models.ForeignKey(Siswa)
    id_mapel = models.ForeignKey(Mapel)
    id_guru = models.ForeignKey(Guru)
    id_kelas = models.ForeignKey(Kelas)
    semester = models.IntegerField()
    harian = models.FloatField(blank=True)
    uts = models.FloatField(blank=True)
    uas = models.FloatField(blank=True)
    tahun_ajaran = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return self.id_siswa.nama
