import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def kirim_email(to_email, subject, message_plain, message_html):
    # Pastikan konfigurasi tidak kosong
    api_key = getattr(settings, "BREVO_API_KEY", None)
    sender_name = getattr(settings, "BREVO_SENDER_NAME", "Sistem Laporan")
    sender_email = getattr(settings, "BREVO_SENDER_EMAIL", None)

    if not api_key or not sender_email:
        logger.error("API Key atau Email Pengirim belum dikonfigurasi di settings.py")
        return None, "Konfigurasi email belum lengkap."

    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": api_key,
        "content-type": "application/json"
    }

    data = {
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
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 201:
            logger.info(f"Email berhasil dikirim ke {to_email}")
        else:
            logger.warning(f"Gagal mengirim email. Status: {response.status_code}, Respon: {response.text}")

        return response.status_code, response.text

    except requests.exceptions.RequestException as e:
        logger.error(f"Kesalahan saat koneksi ke Brevo: {e}")
        return None, str(e)