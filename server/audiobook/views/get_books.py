
from django.http import JsonResponse, HttpRequest
from firebase_admin import storage
import datetime

def get_books(request: HttpRequest):
    try:
        book_name = request.GET.get('book')  

        bucket = storage.bucket()
        blobs = bucket.list_blobs(prefix=book_name)  

        files = []
        for blob in blobs:
            url = blob.generate_signed_url(
                version='v4',
                expiration=datetime.timedelta(days=7), 
                method='GET'
            )

            files.append({
                'name': blob.name,
                'size': blob.size,
                'content_type': blob.content_type,
                'updated': blob.updated.isoformat(),
                'forwarded': url  
            })

        return JsonResponse({'files': files})
    except Exception as e:
        print(e)
        return JsonResponse({"msg": str(e)}, status=500)
