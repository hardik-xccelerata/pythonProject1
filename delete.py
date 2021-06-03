import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/Users/hardikmangal/PycharmProjects/pythonProject1/venv/scripts/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

db.collection('studentdb').document("p1").delete()

db.collection('studentdb').document("a1").update({"age":firestore.DELETE_FIELD})