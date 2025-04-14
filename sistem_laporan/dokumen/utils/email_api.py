import requests
from django.conf import settings

def kirim_email(to_email, subject, message_plain, message_html):
    # Endpoint Brevo API
    url = "https://api.brevo.com/v3/smtp/email"

    # Header dengan API key dari settings
    headers = {
        "accept": "application/json",
        "api-key": settings.BREVO_API_KEY,
        "content-type": "application/json"
    }

    # Data email yang akan dikirim
    data = {
        "sender": {
            "name": settings.BREVO_SENDER_NAME,
            "email": settings.BREVO_SENDER_EMAIL
        },
        "to": [
            {"email": to_email}
        ],
        "subject": subject,
        "htmlContent": message_html,
        "textContent": message_plain
    }

    try:
        # Kirim POST request ke Brevo API
        response = requests.post(url, json=data, headers=headers)

        # Debug print hasil response
        print("===== EMAIL DEBUG INFO =====")
        print("Status Code:", response.status_code)
        print("Response Headers:", response.headers)
        print("Response Body:", response.text)
        print("============================")

        return response.status_code, response.text

    except requests.exceptions.RequestException as e:
        print("Terjadi kesalahan saat mengirim email:", str(e))
        return None, str(e)
