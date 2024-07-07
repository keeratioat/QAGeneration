from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json
app = Flask(__name__)

mysql = MySQL(app)

class Files(Resource):

    def get(self):
        
        path = []
        json_raw = request.get_json()

        sql = "SELECT exam_id FROM exam_detail where exam_name=" +"'"+ json_raw['exam_name']+"';"
        cur2 = mysql.connection.cursor()
        cur2.execute(sql)
        e_id = cur2.fetchall()
        cur2.close()
        print(e_id)

        print(json_raw)
        sql = "SELECT * FROM file_java WHERE exam_id = '" + str(e_id[0][0])+"';"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        file_path = cur.fetchall()
        cur.close()
        for fp in file_path:
            path.append({
                'java_file_path' : fp[2]
            })

        return path

    def post(self):
        json_raw = request.get_json()
        file_path = json_raw["file_path"]
        teacher = json_raw["teacher"]
        print(file_path + " " +teacher)

        sql = "SELECT user_id from user_login where username = '"+teacher+"';"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        u_id = cur.fetchall()
        cur.close()
            
        sql = "INSERT INTO file_java(file_name,user_id) VALUES("+"'"+json_raw['file_path']+"','"+str(u_id[0][0])+"');"
        print(sql)
        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()

        return {"Massage" : "Upload Complete"}