import pymongo


client = pymongo.MongoClient("mongodb+srv://pawan54463:9470754463@cluster0.8v0ehaf.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database["pawan"]


#data = collection.find({"companyName": "iNeuron"})#
data = collection.find({"courseOffered" : {"$gt": "E"}})
for i in data:
    print(i)



