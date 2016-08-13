from __future__ import unicode_literals

from django.db import models
from django.db.models.fields.files import *
from django.conf import settings
# Create your models here.

class Guru(models.Model):
    nip = models.CharField(max_length=20, primary_key=True)
    nama = models.CharField(max_length=50)
    alamat = models.TextField(blank=True)
    tgl_lahir = models.DateField()
    telepon = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    foto = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT, "upload/guru"), blank=True)

    def __unicode__(self):
        return self.nip

