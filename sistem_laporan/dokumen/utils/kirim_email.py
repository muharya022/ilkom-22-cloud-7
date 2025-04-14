from dokumen.utils.email_api import kirim_email

def kirim_email_setelah_upload(user_email):
    subject = "Laporan Berhasil Diunggah"
    plain = "Terima kasih, laporan Anda sudah berhasil diunggah ke sistem."
    html = "<p><strong>Terima kasih</strong>, laporan Anda sudah berhasil diunggah ke sistem.</p>"

    status, response = kirim_email(user_email, subject, plain, html)

    print(f"Status pengiriman: {status}")
    print(f"Respon dari Brevo: {response}")
