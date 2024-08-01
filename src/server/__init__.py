from .firebase import cred
import firebase_admin

firebase_admin.initialize_app(cred,{
    'storageBucket': 'sih-projec.appspot.com'  # Replace with your bucket name
})
