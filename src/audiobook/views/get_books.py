
from django.http import JsonResponse, HttpRequest
from firebase_admin import storage

def get_books(request: HttpRequest):
    try: 
        bucket = storage.bucket()
        blobs = bucket.list_blobs()  
        
        files = []
        for blob in blobs:
            uuid_name=blob.name.split('_$_')
            files.append({
                'name': uuid_name[1],
                'forward':blob.name
            })

        return JsonResponse({'files': files})
    except Exception as e:
        print(e)
        return JsonResponse({"msg": str(e)}, status=500)
