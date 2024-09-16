from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
# Import the update_expense function from the appropriate module
from .expense import update_expense

@csrf_exempt
def update_expense_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            project_id = data.get('project_id')
            expense_id = data.get('expense_id')
            pdf_drive_id = data.get('pdf_drive_id')

            if not project_id or not expense_id or not pdf_drive_id:
                return JsonResponse({'error': 'Missing required parameters'}, status=400)

            moco_api_key = os.getenv("MOCO_API_KEY")
            moco_domain = os.getenv("MOCO_DOMAIN")

            result = update_expense(project_id, expense_id, pdf_drive_id, moco_api_key, moco_domain)
            print("Result: ", result)
            if result:
                return JsonResponse(result, status=200)
            else:
                return JsonResponse({'error': 'Failed to update expense'}, status=500)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)