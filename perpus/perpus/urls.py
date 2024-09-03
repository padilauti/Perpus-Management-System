from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from perpustakaan.views import buku, penerbit, tambah_buku, ubah_buku, hapus_buku, signup, export_xlsx



urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku, name='buku'),
    path('penerbit/', penerbit, name='penerbit'),
    path('tambah-buku/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name='hapus_buku'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('signup/', signup, name='signup'),
    path('export/xlsx/', export_xlsx, name='export_xlsx'),
]
