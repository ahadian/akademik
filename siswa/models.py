from __future__ import unicode_literals

from kelas.models import *
from django.db.models.fields.files import *
from django.conf import settings


# Create your models here.

class Siswa(models.Model):
    PILIH_JURUSAN = (
        ('ipa','IPA'),
        ('ips','IPS'),
        ('belum','Belum'),
    )
    nis = models.CharField(primary_key=True, max_length=20)
    nama = models.CharField(max_length=50)
    alamat = models.TextField(blank=True)
    tgl_lahir = models.DateField()
    tahun_masuk = models.CharField(max_length=4)
    jurusan = models.CharField(max_length=5, choices=PILIH_JURUSAN)
    kelas_sekarang = models.ForeignKey(Kelas, null=True)
    foto = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT, "upload/siswa"), blank=True)
    def __unicode__(self):
        return self.nis

