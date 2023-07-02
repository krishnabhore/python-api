import mysql.connector
import json

class database:
    
    def __init__(self):
        self.connect=mysql.connector.connect(host="localhost",port="3312",username="root",password="mysqltest",database="classicmodels")
        self.connect.autocommit=True
        print(self.connect)
        print("connection successful")  

    def getData(self):
        self.cursor=self.connect.cursor(dictionary=True)
        self.cursor.execute("SELECT * FROM data")
        result=self.cursor.fetchall()
        # print(json.dumps(result))
        return json.dumps(result)
    
    def insertData(self,data):
        self.cursor=self.connect.cursor(dictionary=True)
        print(data)
        self.cursor.execute(f"INSERT INTO data(name,state,city) VALUES('{data['name']}','{data['state']}','{data['city']}')")
        return "Insert data successfully"




# obj=database()
# obj.connection()
    