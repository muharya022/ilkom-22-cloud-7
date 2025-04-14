from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Dokumen, Laporan
from .forms import LaporanForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

@login_required(login_url='login')
def unggah_laporan(request, dokumen_id):
    dokumen = get_object_or_404(Dokumen, id=dokumen_id)
    laporan, created = Laporan.objects.get_or_create(dokumen=dokumen)

    if request.method == "POST":
        form = LaporanForm(request.POST, request.FILES, instance=laporan, dokumen=dokumen)
        if form.is_valid():
            if 'file' in request.FILES:
                form.save()
                dokumen.laporan_diunggah = True
                dokumen.status = "Sudah Diunggah"
                dokumen.save()
                messages.success(request, "Laporan berhasil diperbarui!")
                return redirect("daftar_dokumen")
            else:
                messages.error(request, "Anda harus mengunggah file laporan terlebih dahulu.")
        else:
            messages.error(request, "Terjadi kesalahan. Periksa kembali data yang Anda masukkan.")
    else:
        form = LaporanForm(instance=laporan, dokumen=dokumen)

    return render(request, "dokumen/unggah_laporan.html", {"form": form, "dokumen": dokumen})