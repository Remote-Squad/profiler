import requests
import base64
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from dotenv import load_dotenv
import os
import json

import logging 
# Set up the basic configuration for logging
logging.basicConfig(
    filename='/home/mainfilm/logs/my_log_file.log',  # PythonAnywhere path to logs
    level=logging.ERROR,  # Log errors and above (i.e., warnings, critical errors)
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log an error message
logging.error('An error occurred in the application!')


# Get the absolute path of the current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path for the service account file
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'service_account.json')



load_dotenv()

moco_api_key = os.getenv("MOCO_API_KEY")
moco_domain =os.getenv("MOCO_DOMAIN")

# Note the API KEY FOR MOCO MUS BE A MASTER NOTA A SPECIFIC ACCOUNT
def download_gdrive_file_to_base64(gdrive_id):
    try:
        SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('drive', 'v3', credentials=credentials)

        file_content = io.BytesIO()
        request = service.files().get_media(fileId=gdrive_id)
        downloader = MediaIoBaseDownload(file_content, request)

        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}% complete.")

        file_content.seek(0)
        return base64.b64encode(file_content.read()).decode('utf-8')
    except Exception as e:
        print(f"Failed to download and encode file: {str(e)}")

        return None

def update_expense(project_id, expense_id, pdf_drive_id, moco_api_key, moco_domain):
    base_url = f"https://{moco_domain}.mocoapp.com/api/v1"
    headers = {
        "Authorization": f"Token token={moco_api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(f"{base_url}/projects/{project_id}/expenses/{expense_id}", headers=headers)
        response.raise_for_status()
        current_expense = response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch current expense: {str(e)}")
        return None

    pdf_base64 = pdf_drive_id
    if not pdf_base64:
        print("Failed to download and encode the PDF file.")

        return None

    new_expense_data = {
        "date": current_expense["date"],
        "title": current_expense["title"] + " (Updated)",
        "quantity": current_expense["quantity"],
        "unit": current_expense["unit"],
        "unit_price": current_expense["unit_price"],
        "unit_cost": current_expense["unit_cost"],
        "file": {
            "filename": "updated_document.pdf",
            "base64": pdf_base64
        },
        "company": current_expense.get("company", {}),
        "project": current_expense.get("project", {}),
        "group": current_expense.get("group", {}),
        "created_at": current_expense.get("created_at"),
        "updated_at": current_expense.get("updated_at")
    }

    try:
        response = requests.post(f"{base_url}/projects/{project_id}/expenses", headers=headers, json=new_expense_data)
        response.raise_for_status()
        new_expense = response.json()
    except requests.RequestException as e:
        print(f"Failed to create new expense: {str(e)}")
        return None

    try:
        response = requests.delete(f"{base_url}/projects/{project_id}/expenses/{expense_id}", headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to delete old expense: {str(e)}")
        return None

    return new_expense

if __name__ == '__main__':
    project_id = "947039913"
    expense_id = "3155881"
    pdf_drive_id = "1IBFRsaRSCxNhcQGddyeZYAEkEyLi-SCV"

    result = update_expense(project_id, expense_id, pdf_drive_id, moco_api_key, moco_domain)
    if result:
        print(json.dumps(result, indent=2))
    else:
        print("Failed to update expense.")

