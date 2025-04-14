# dokumen/utils/email_api.py
import requests

BREVO_API_KEY = "BREVO_API_KEY"  # Ganti ini di production!

def kirim_email(to_email, subject, message_plain, message_html):
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }
    data = {
        "sender": {
            "name": "Sistem Laporan",
            "email": "mitra2704@gmail.com"
        },
        "to": [
            {"email": to_email}
        ],
        "subject": subject,
        "htmlContent": message_html,
        "textContent": message_plain
    }

    response = requests.post(url, json=data, headers=headers)

    print("Status kirim email:", response.status_code)
    print("Respon dari Brevo:", response.text)

    return response.status_code, response.text