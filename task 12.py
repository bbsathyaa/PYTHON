import  json
x={
    "Name":"John",
    "Age":30,
    "city":"New York",
    "grade": None,
    "result": True,
    "marks1":{"maths":98,"CS":99},
    "marks2":[90,98,89],
    "avg":97.99
}
y=json.dumps(x)
print(y)
print(json.dumps((1,2,3)))
print(json.dumps(list(range(9))))

from pymongo import MongoClient
myclient=MongoClient("mongodb://localhost:27017/") #making connection
db=myclient["ABC"] #database
Collection=db["data"]
with open('D:\\Python Internship\\task12\\data.json') as f:
    file_data=json.load(f)
if isinstance(file_data,list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)
