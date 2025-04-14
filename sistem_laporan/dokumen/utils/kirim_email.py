from dokumen.utils import email_api

def kirim_email_dev():
    email = "devtester@example.com"
    subject = "Cek Pengiriman Email Dev"
    plain = "Ini adalah pengujian dari environment development."
    html = "<p>Ini adalah <strong>pengujian</strong> dari environment development.</p>"

    print(f"Simulasi pengiriman email ke {email} berhasil.")
