import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/Users/hardikmangal/PycharmProjects/pythonProject1/venv/scripts/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

student_data = {}

for x in range(8):
    name = input('Enter name: ')
    age = input('Enter age: ')
    gender = input('enter gender')
    city = input('enter city')
    student_data['name'] = name
    student_data['age'] = age
    student_data['gender'] = gender
    student_data['city'] = city
    db.collection('studentdb').add(student_data)

student_marks ={}
for x in range(3) :
    subject = input('enter subject: ')
    marks = input('marks')
    student_marks['subject'] = subject
    student_marks['marks'] = marks
    db.collection('studentdb').document('a1').collection('subject_marks').add(student_marks)

data1={'name':'neetu', 'age':23, 'gender':'female'}
db.collection('studentdb').document('a1').set(data1)

db.collection('studentdb').document('a1').set({'city':'kolkata'},merge=True)
