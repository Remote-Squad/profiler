from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
# Import the update_expense function from the appropriate module
from .expense import update_expense
import base64
from django.views.decorators.http import require_POST
import pdfplumber

# Max content length in bytes (16 MB) for the PDF file (extract_text view)
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB


@csrf_exempt
def update_expense_view(request):
    if request.method == 'POST':

        try:
            project_id = request.POST.get('project_id')
            expense_id = request.POST.get('expense_id')


            pdf_drive_id = request.FILES.get('pdf_drive_id')
            print("pdf_data")

            print(pdf_drive_id)

            if not project_id or not expense_id or not pdf_drive_id:
                return JsonResponse({'error': 'Missing required parameters'}, status=400)

            # Read the PDF file in binary mode
            pdf_drive_id = pdf_drive_id.read()

            # Convert the binary content into a base64-encoded string
            pdf_base64 = base64.b64encode(pdf_drive_id).decode('utf-8')

            moco_api_key = os.getenv("MOCO_API_KEY")
            moco_domain = os.getenv("MOCO_DOMAIN")

            result = update_expense(project_id, expense_id, pdf_base64, moco_api_key, moco_domain)
            print("Result: ", result)
            if result:
                return JsonResponse(result, status=200)
            else:
                print("'error': 'Failed to update expense'")
                return JsonResponse({'error': 'Failed to update expense'}, status=500)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            print(f'1-error {str(e)}')
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


# Max content length in bytes (16 MB)
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB


@csrf_exempt  # Only needed if CSRF protection isn't required, e.g., for APIs
@require_POST
def extract_text(request):
    # Check if the request contains a file
    if 'file' not in request.FILES:
        return JsonResponse({'error': 'No file part in the request.'}, status=400)

    file = request.FILES['file']

    # Check for empty filename
    if file.name == '':
        return JsonResponse({'error': 'No file selected for uploading.'}, status=400)

    # Check file type and size
    if file.content_type == 'application/pdf' and file.size <= MAX_CONTENT_LENGTH:
        try:
            # Extract text from the PDF file
            with pdfplumber.open(file) as pdf:
                full_text = ''
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        full_text += text + '\n'
            return JsonResponse({'extracted_text': full_text}, status=200)
        except Exception as e:
            return JsonResponse({'error': f'Error processing PDF: {str(e)}'}, status=500)
    else:
        return JsonResponse(
            {'error': 'Invalid file type or file size too large. Only PDF files under 16 MB are allowed.'}, status=400)
