from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django import template

#from raport.forms import InputRaport
from raport.models import Raport
from siswa.models import *

# Create your views here.

@login_required(login_url=settings.LOGIN_URL_SISWA)
def lihat_raport(request):
    siswa = Siswa.objects.get(nis = request.session['siswa_id'])
    nilai = Raport.objects.filter(id_siswa=request.session['siswa_id'])
    sms = Raport.objects.all().values('semester').distinct()


    if request.method == 'POST':
        sem = request.POST['data-semester']
        nilai = Raport.objects.filter(id_siswa=request.session['siswa_id'], semester=sem)
    return render(request, 'raport.html', {"sms":sms,"nilai": nilai, "siswa":siswa})


@login_required(login_url=settings.LOGIN_URL_GURU)
def input_raport (request):
    mapel = Pengajar.objects.filter(kd_guru_id=request.session['guru_id'])
    guru = Guru.objects.get(nip=request.session['guru_id'])
    siswa = Raport.objects.filter(id_guru=request.session['guru_id'])
    if request.method == 'POST':
        nama_kelas = request.POST['nama_kelas']
        nama_mapel = request.POST['nama_mapel']
        siswa = Raport.objects.filter(id_guru=request.session['guru_id'],id_kelas_id=nama_kelas, id_mapel = nama_mapel)


    return render(request, 'input-raport.html',{"mapel":mapel,"siswa":siswa, "guru":guru})

@login_required(login_url=settings.LOGIN_URL_GURU)
def input (request):
    mapel = Pengajar.objects.filter(kd_guru_id=request.session['guru_id'])
    input_nilai = Raport.objects.filter(id_guru=request.session['guru_id'])
    guru = Guru.objects.get(nip=request.session['guru_id'])
    nip = Guru.objects.filter(nip=request.session['guru_id'])

    siswa = Siswa.objects.all()


    if request.method == 'POST':
        nilai = Raport(
            id_siswa_id=request.POST['id_siswa'],
            semester=request.POST['semester'],
            id_guru_id = request.POST['id_guru'],
            id_kelas_id = request.POST['kelas'],
            id_mapel_id = request.POST['mapel'],
            harian = request.POST['harian'],
            uts=request.POST['uts'],
            uas=request.POST['uas'],
            tahun_ajaran=request.POST['tahun_ajaran'],
        )
        try:
            nilai.save()
        except ValueError:
            harianTest = request.POST['harian']
            utsTest = request.POST['uts']
            uasTest = request.POST['uas']

            if harianTest == '':
                harianTest = 0
            if utsTest == '':
                utsTest = 0
            if uasTest == '':
                uasTest = 0

            nilai = Raport(
                id_siswa_id=request.POST['id_siswa'],
                semester=request.POST['semester'],
                id_guru_id=request.POST['id_guru'],
                id_kelas_id=request.POST['kelas'],
                id_mapel_id=request.POST['mapel'],
                harian=harianTest,
                uts=utsTest,
                uas=uasTest,
            )
            nilai.save()
        return redirect('/input-nilai/')
    return render(request, 'input.html', {"nip":nip,"input_nilai":input_nilai,"mapel":mapel,"siswa":siswa, "guru":guru})

@login_required(login_url=settings.LOGIN_URL_GURU)
def update (request):
    if request.method == 'POST':
        if request.method == 'POST':
                nilai = Raport(
                    id = request.POST['id'],
                    id_siswa_id=request.POST['nis'],
                    semester=request.POST['semester'],
                    id_guru_id=request.session['guru_id'],
                    id_kelas_id=request.POST['kelas'],
                    id_mapel_id=request.POST['mapel'],
                    harian=request.POST['harian'],
                    uts=request.POST['uts'],
                    uas=request.POST['uas'],
                    tahun_ajaran=request.POST['tahun_ajaran']
                )
                try:
                    nilai.save()
                except ValueError:
                    harianTest = request.POST['harian']
                    utsTest = request.POST['uts']
                    uasTest = request.POST['uas']

                    if harianTest == '':
                        harianTest = 0
                    if utsTest == '':
                        utsTest = 0
                    if uasTest == '':
                        uasTest = 0

                    nilai = Raport(
                        id=request.POST['id'],
                        id_siswa_id=request.POST['nis'],
                        semester=request.POST['semester'],
                        id_guru_id=request.session['guru_id'],
                        id_kelas_id=request.POST['kelas'],
                        id_mapel_id=request.POST['mapel'],
                        harian=harianTest,
                        uts=utsTest,
                        uas=uasTest,
                    )
                    nilai.save()



    return redirect('/input-nilai/')


@login_required(login_url=settings.LOGIN_URL_GURU)
def hapus(request):
    if request.method == 'POST':
        id = request.POST['id']
        data = Raport.objects.get(id=id)
        data.delete()
        return redirect('/input-nilai/')
