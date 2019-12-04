import os
import firebase_admin
from firebase_admin import credentials, firestore
import google.cloud.exceptions

def initFirebase():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path_to_cert = BASE_DIR + "/cs411collegeadvising-firebase-adminsdk-pzxxz-3690912db1.json"
    cred = credentials.Certificate(path_to_cert)
    firebase_admin.initialize_app(cred)

initFirebase()

def readProfileFirebase(userId):
    db = firestore.client()
    profile = None
    try:
        profileDocument = db.collection('profiles').document(str(userId)).get()
        profile = profileDocument.to_dict()
        print('Document data: {}'.format(profile))
    except google.cloud.exceptions.NotFound:
        print('No such document!')
    return profile