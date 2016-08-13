from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from siswa.models import Siswa
# Create your views here.

@login_required(login_url=settings.LOGIN_URL_SISWA)
def profil(request):
    siswa = Siswa.objects.get(nis=request.session['siswa_id'])
    return render(request, 'profil-siswa.html', {"siswa": siswa})

@login_required(login_url=settings.LOGIN_URL_SISWA)
def ganti_foto(request):
    siswa = Siswa.objects.get(nis=request.session['siswa_id'])
    siswa.foto = request.FILES['files']
    siswa.save()

    return redirect('/profil-siswa/')
