import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def kirim_email(to_email, subject, message_plain, message_html):
    # Ambil konfigurasi dari settings.py
    api_key = getattr(settings, 'BREVO_API_KEY', None)
    sender_email = getattr(settings, 'BREVO_SENDER_EMAIL', None)
    sender_name = getattr(settings, 'BREVO_SENDER_NAME', 'Sistem Laporan')

    if not api_key or not sender_email:
        logger.error("BREVO_API_KEY atau BREVO_SENDER_EMAIL belum diatur di settings.py")
        return None, "Konfigurasi belum lengkap"

    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json"
    }

    payload = {
        "sender": {
            "name": sender_name,
            "email": sender_email
        },
        "to": [{"email": to_email}],
        "subject": subject,
        "htmlContent": message_html,
        "textContent": message_plain
    }

    try:
        response = requests.post(url, json=payload, headers=headers)

        # Log respon dari Brevo
        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response: {response.text}")

        if response.status_code == 201:
            print("✅ Email berhasil dikirim ke", to_email)
        else:
            print("⚠️ Gagal kirim email.")
            print("Status:", response.status_code)
            print("Response:", response.text)

        return response.status_code, response.text

    except Exception as e:
        logger.error("❌ Gagal koneksi ke Brevo:", exc_info=e)
        return None, str(e)