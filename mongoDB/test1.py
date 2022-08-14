import pymongo
client = pymongo.MongoClient("mongodb+srv://pawan54463:9470754463@cluster0.8v0ehaf.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "pawan",
    "mail_id" : "pawanaryan93@gmail.com",
    "surname" : "kumar"
}
db1 = client['mongoDB']
coll = db1['test']
coll.insert_one(d)