from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from guru.models import Guru
# Create your views here.

@login_required(login_url=settings.LOGIN_URL_GURU)
def profil(request):
    guru = Guru.objects.get(nip=request.session['guru_id'])
    return render(request, 'profil-guru.html', {"guru": guru})

@login_required(login_url=settings.LOGIN_URL_GURU)
def ganti_foto(request):
    guru = Guru.objects.get(nip=request.session['guru_id'])
    guru.foto = request.FILES['files']
    guru.save()

    return redirect('/profil-guru/')


