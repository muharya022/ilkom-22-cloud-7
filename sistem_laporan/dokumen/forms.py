from django import forms
from .models import Dokumen, Laporan
import json

class DokumenForm(forms.ModelForm):
    IRBAN_CHOICES = [
        ("IRBAN 1", "IRBAN 1"),
        ("IRBAN 2", "IRBAN 2"),
        ("IRBAN 3", "IRBAN 3"),
        ("IRBAN 4", "IRBAN 4"),
        ("IRBAN INVESTIGASI", "IRBAN INVESTIGASI"),
    ]

    class Meta:
        model = Dokumen
        fields = ["nomor_surat", "tanggal_surat", "irban", "tim_audit", "uraian", "file"]
        widgets = {
            "nomor_surat": forms.TextInput(attrs={"class": "form-control", "placeholder": "Masukkan nomor surat"}),
            "tanggal_surat": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "file": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def clean_tim_audit(self):
        """Pastikan tim audit berbentuk JSON valid."""
        tim_audit_data = self.cleaned_data.get("tim_audit")
        try:
            if tim_audit_data:
                return json.loads(tim_audit_data)
            return []
        except json.JSONDecodeError:
            raise forms.ValidationError("Format data tim audit tidak valid.")
