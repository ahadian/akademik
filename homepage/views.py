from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.conf import settings

from akun.models import AkunSiswa, AkunGuru
from siswa.models import Siswa


# Create your views here.

def login_siswa(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                try:
                    akun = AkunSiswa.objects.get(akun=user.id)
                    login(request, user)

                    request.session['siswa_id'] = akun.siswa.nis
                    request.session['jenis_akun'] = akun.jenis_akun
                    request.session['username'] = request.POST['username']
                except:
                    messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data siswa, silakan hubungi administrator')
                return redirect('/profil-siswa/')
            else:
                messages.add_message(request, messages.INFO, 'User belum terverifikasi')
        else:
            messages.add_message(request, messages.INFO, 'Username dan Password Salah')
    return render(request, 'login-siswa.html')


def out(request):
    logout(request)
    return redirect('/')

def login_guru(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                try:
                    akun = AkunGuru.objects.get(akun=user.id)
                    login(request, user)

                    request.session['guru_id'] = akun.guru.nip
                    request.session['jenis_akun'] = akun.jenis_akun
                    request.session['username'] = request.POST['username']
                except:
                    messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data guru, silakan hubungi administrator')
                return redirect('/profil-guru/')
            else:
                messages.add_message(request, messages.INFO, 'User belum terverifikasi')
        else:
            messages.add_message(request, messages.INFO, 'Username dan Password Salah')
    return render(request, 'login-guru.html')



def index(request):
    return render(request, 'utama.html')

def handler404(request, param):
    if not param:

        return HttpResponseNotFound('404.html')
    return render_to_response('404.html')

def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
