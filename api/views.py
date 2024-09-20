from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
# Import the update_expense function from the appropriate module
from .expense import update_expense
import base64

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