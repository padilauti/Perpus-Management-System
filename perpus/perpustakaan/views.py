from django.shortcuts import render, redirect, HttpResponse
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from perpustakaan.resource import BukuResource



def export_xlsx(request):
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="laporan buku.xlsx"'
    return response

    
@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User berhasil dibuat!")
            return redirect('signup')
        else:
            messages.success(request, "Terjadi kesalahan!")
            return redirect('signup')
        
    else:
        form = UserCreationForm()
        context = {
            'form': form,
        }
    return render(request, 'signup.html', context)


@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()

    messages.success(request, "Data Berhasil dihapus!!!")
    return redirect('buku')

@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berasil diperbaruhin !!!")
            return redirect('ubah_buku', id_buku=id_buku)
        
    else:
        form = FormBuku(instance=buku)
        context = {
            'form': form,
            'buku': buku,
        }

    return render(request, template, context)
    
@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    # select * from Buku where jumlah=90
    # books = Buku.objects.all() # ini buat menampilkan semua data
    # [:3] untuk menampilkan limit 
    # books = Buku.objects.filter(kelompok_id__nama='Produktif')[:3]
    # books = Buku.objects.filter(jumlah=100)

    books = Buku.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'buku.html', context)


@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    return render(request, 'penerbit.html')

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku
            pesan = "Data Berhasil Disimpan"

            context = {
                'form': form,
                'pesan' : pesan,
            }
            return render(request, 'tambah-buku.html', context)
    else:
        form = FormBuku()

        context = {
            'form': form,
        }

    return render(request, 'tambah-buku.html', context)