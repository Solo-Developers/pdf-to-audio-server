import firebase_admin
import os
from firebase_admin import credentials

cred = credentials.Certificate(os.path.join(os.getcwd(),"..","firebase-key.json"))

