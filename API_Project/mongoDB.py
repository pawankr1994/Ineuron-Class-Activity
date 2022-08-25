from flask import Flask, request, jsonify

import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://pawan54463:mongo9470754463@cluster0.8v0ehaf.mongodb.net/?retryWrites=true&w=majority")
database = client['taskdb']
collection = database ['taskcollection']




@app.route("/insert", methods = ['POST'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return jsonify(str('Succesfully inserted'))

if __name__ == '__main__':
    app.run(port = 5003)



