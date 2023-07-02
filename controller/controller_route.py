from app import app
from Model.model import registration
from Model.db_connect import database
from flask import Flask, request
r=registration()
obj=database()



@app.route("/singup")
def singup():
    return "Signup PAGE"

@app.route("/login")
def login():
    return "Login PAGE"

@app.route("/singup/register")
def register():
    return r.register_details()

@app.route("/user/getdata")
def user_details():
    return obj.getData() 

@app.route("/user/insertdata", methods=['POST'])
def insert_details():
    # print(request.form)
    return obj.insertData(request.form)

