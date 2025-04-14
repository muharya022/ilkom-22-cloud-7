from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from datetime import timedelta

class Dokumen(models.Model):
    IRBAN_CHOICES = [
        ("IRBAN 1", "IRBAN 1"),
        ("IRBAN 2", "IRBAN 2"),
        ("IRBAN 3", "IRBAN 3"),
        ("IRBAN 4", "IRBAN 4"),
        ("IRBAN INVESTIGASI", "IRBAN INVESTIGASI"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nomor_surat = models.CharField(max_length=100, unique=True)
    irban = models.CharField(max_length=20, choices=IRBAN_CHOICES)
    tim_audit = models.JSONField(default=list)
    uraian = models.CharField(max_length=255)
    file = models.FileField(upload_to="dokumen/")
    created_at = models.DateTimeField(auto_now_add=True)
    laporan_diunggah = models.BooleanField(default=False)
    tanggal_surat = models.DateField()