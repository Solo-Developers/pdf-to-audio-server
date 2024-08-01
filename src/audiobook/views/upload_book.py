#  under dev
from firebase_admin import storage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import uuid

@csrf_exempt
def upload_book(request):
    if request.method != 'POST':
        return JsonResponse({"msg": "Only POST requests are allowed"}, status=405)

    # Get book file from the request
    file = request.FILES.get('file')
    if not file:
        return JsonResponse({"msg": "File not found"}, status=400)
    if file.content_type != 'application/pdf':
        return JsonResponse({"msg": "File type not supported. Only PDF files are allowed."}, status=400)
    
    try:
        random_uuid = uuid.uuid4()
        file_name=file.name.split('.')[0]
        bucket=storage.bucket()
        blob = bucket.blob(f'{random_uuid}_$_{file_name}')
        blob.content_type='application/pdf'
        blob.upload_from_file(file)
    except Exception as e:
        return JsonResponse({"msg": f"Error uploading file to Firebase Storage: {e}"}, status=500)

    return JsonResponse({"msg": "File uploaded successfully"}, status=200)