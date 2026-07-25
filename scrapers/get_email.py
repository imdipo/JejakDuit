import os
import base64
import time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "credentials.json"))
TOKEN_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "token.json"))

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def gmail_login():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())
        
    
    return build("gmail", "v1", credentials=creds)

def read_gmail():
    daftar_html_mentah = []
    service = gmail_login()

    sekarang = int(time.time())
    kemarin = sekarang - 86400

    query = f'from:noreply.livin@bankmandiri.co.id "detail transaksi" after:{kemarin} before:{sekarang}'

    # minta daftar id email yang sesuai dengan query
    hasil = service.users().messages().list(userId="me", q=query).execute()
    messages = hasil.get("messages", [])

    if not messages:
        print("tidak ada email mandiri baru")
        return

    print(f"ada! ketemu {len(messages)} email dari bank mandiri")
    
    for message in messages:
        pesan = service.users().messages().get(userId="me", id=message["id"], format="full").execute()

        # ekstrak
        payload = pesan["payload"]
        if "parts" in payload:
            parts = payload["parts"]
            body = parts[0]["body"].get("data", "")
        else: body = payload["body"].get("data", "")

        if body:
            html_mentah = base64.urlsafe_b64decode(body).decode("utf-8")
            daftar_html_mentah.append(html_mentah)
    
    return daftar_html_mentah