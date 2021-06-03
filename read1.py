import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/Users/hardikmangal/PycharmProjects/pythonProject1/venv/scripts/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

dat = db.collection('studentdb').get()
for data in dat:
    print(data.to_dict())

result = db.collection('studentdb').document("p1").get()
print(result.to_dict())

result = db.collection('studentdb').document("a1").get()
print(result.to_dict())

dat = db.collection('studentdb').document("a1").collection('subject_marks').get()
for data in dat:
    print(data.to_dict())

dat = db.collection('studentdb').where("age", "==", "21").get()
for data in dat:
    print(data.to_dict())

dat = db.collection('studentdb').where("age", ">", "22").get()
for data in dat:
    print(data.to_dict())

dat = db.collection('studentdb').where("city", "==", "delhi").get()
for data in dat:
    print(data.to_dict())