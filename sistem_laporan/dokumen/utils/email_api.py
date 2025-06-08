import os
import requests
from dotenv import load_dotenv

load_dotenv()  # load environment variables dari .env

BREVO_API_KEY = os.getenv("BREVO_API_KEY")

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
            "email": "muhammadaryaalfajar@gmail.com"
        },
        "to": [{"email": to_email}],
        "subject": subject,
        "htmlContent": message_html,
        "textContent": message_plain
    }

    response = requests.post(url, json=data, headers=headers)
    print("Status kirim email:", response.status_code)
    print("Respon dari Brevo:", response.text)

    return response.status_code, response.text
