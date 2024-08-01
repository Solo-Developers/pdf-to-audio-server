from django.http import JsonResponse
from firebase_admin import storage
import pymupdf


def get_book(request):
    if request.method != 'GET':
        return JsonResponse({"msg": "Only GET requests are allowed"}, status=405)

    # Retrieve the book name from the query parameters
    book_name = request.GET.get('book')
    if not book_name:
        return JsonResponse({"msg": "Book name is required"}, status=400)

    try:
        # Get the storage bucket
        bucket = storage.bucket()

        # Retrieve the blob using the book name
        blob = bucket.get_blob(book_name)
        if blob is None:
            return JsonResponse({"msg": "File not found"}, status=404)
        

        pdf_bytes = blob.download_as_bytes()
        doc= pymupdf.open(stream=pdf_bytes, filetype='pdf')
        text = ""
        for page in doc:
            page_text = page.get_text()
            page_text = page_text.replace('\n', ' ').replace('\t', ' ').strip()
            page_text = ' '.join(page_text.split())
            text += page_text + ' '  

        # # Return the extracted text as a JSON response
        
        return JsonResponse({
            "msg": "File processed successfully",
            "text": text
        })

    except Exception as e:
        return JsonResponse({"msg": f"Error processing file: {e}"}, status=500)
