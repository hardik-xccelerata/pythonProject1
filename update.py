import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/Users/hardikmangal/PycharmProjects/pythonProject1/venv/scripts/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

db.collection('studentdb').document("a1").update({"age": 50})

db.collection('studentdb').document("p1").update({"age": firestore.Increment(2)})

db.collection('studentdb').document("DZ9utt0pw2cO0RMIFEaT").update({"gender": "female"})

db.collection('studentdb').document("p1").update({"occupation": "engineer"})

dat = db.collection('studentdb').where("age", ">", 20).get() # Get all documents with age >=40
for data in dat:
    key = data.id
    db.collection('studentdb').document(key).update({"age_group":"youth"})