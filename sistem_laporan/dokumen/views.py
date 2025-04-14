from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Dokumen, Laporan
from .forms import DokumenForm, LaporanForm
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.utils.timezone import now
import json

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


@login_required(login_url='login')
def unggah_dokumen(request):
    if request.method == "POST":
        form = DokumenForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                dokumen = form.save(commit=False) 
                dokumen.user = request.user  
                dokumen.save()

                tim_audit_data = request.POST.get("tim_audit")
                if tim_audit_data:
                    try:
                        dokumen.tim_audit = json.loads(tim_audit_data)
                    except json.JSONDecodeError:
                        dokumen.tim_audit = []
                    dokumen.save()
                
                messages.success(request, "Surat Tugas berhasil diunggah.")
                return redirect("daftar_dokumen")
            except IntegrityError:
                messages.error(request, "Nomor surat sudah digunakan. Gunakan nomor yang berbeda.")
        else:
            print("Form Errors:", form.errors)
            messages.error(request, "Terjadi kesalahan, pastikan semua data telah diisi dengan benar.")
    else:
        form = DokumenForm()

    return render(request, "dokumen/unggah_dokumen.html", {"form": form,})
