from flask_pymongo import pymongo
from flask import jsonify, request
import pandas as pd

con_string = "mongodb+srv://prathip:prathip@prathipcluster.8vlxkkg.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_string)
db = client.get_database('testdb')

user_collection = pymongo.collection.Collection(db, 'users')
collection = user_collection.testdb.users
print("MongoDB connected Successfully")


def api_routes(endpoints):
    
    @endpoints.route('/post_users', methods=['POST'])
    def post_user():
        resp = {}
        try:
            req_body = request.json
            user_collection.insert_one(req_body)            
            print("User Data Stored Successfully in the MangoDB.")
            status = {
                "statusCode":"200",
                "req_body":req_body,
                "statusMessage":"User Data Stored Successfully in the MangoDB."
            }
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)
            }
        resp["status"] =status
        return resp


   

    @endpoints.route('/get_users',methods=['GET'])
    def get_users():
        resp = {}
        try:
            users = user_collection.find({})
            users = list(users)
            status = {
                "statusCode":"200",
                "statusMessage":"User Data Retrieved Successfully from the MangoDB."
            }
            output = [{'Id' : user['id'],'Name' : user['name'], 'Age' :user['age']} for user in users]   #list comprehension
            resp['data'] = output
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)
            }
        resp["data"] =output
        return resp

    @endpoints.route('/put_users',methods=['PUT'])
    def put_users():
        resp = {}
        try:
            req_body = request.json
            user_collection.update_one({"id":req_body['id']}, {"$set": req_body})
            print("User Data Updated Successfully in the Database.")
            status = {
                "statusCode":"200",
                "req_body":req_body,
                "statusMessage":"User Data Updated Successfully in the MangoDB."
            }
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)
            }
        resp["status"] =status
        return resp    

    @endpoints.route('/delete_users',methods=['DELETE'])
    def delete_users():
        resp = {}
        try:
            req_body = request.json
            user_collection.delete_one(req_body)
            status = {
                "statusCode":"200",
                "req_body":req_body,
                "statusMessage":"User Data Deleted Successfully in the MangoDB."
            }
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)
            }
        resp["status"] =status
        return resp
    


    return endpoints
