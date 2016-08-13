"""akademik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from django.templatetags.static import static
from django.conf.urls import handler404



from homepage import views as homepage_views
from siswa import views as siswa_views
from guru import views as guru_views
from raport import views as raport_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login-siswa/', homepage_views.login_siswa),
    url(r'^logout/', homepage_views.out),
    url(r'^profil-siswa/', siswa_views.profil),
    url(r'^profil-guru/', guru_views.profil),
    url(r'^$', homepage_views.index),
    url(r'^login-guru/', homepage_views.login_guru),
    url(r'^lihat-nilai/', raport_views.lihat_raport),
    url(r'^input-nilai/', raport_views.input_raport),
    url(r'^ganti_foto/', siswa_views.ganti_foto),
    url(r'^input/', raport_views.input),
    url(r'^up/', raport_views.update),
    url(r'^del/', raport_views.hapus),
    url(r'^change/', guru_views.ganti_foto),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = homepage_views.handler404
handler500 = homepage_views.handler500