from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)
class ShowAnwserStd(Resource):
    def get(self):
        json_raw = request.get_json()

        sql = "SELECT exam_id FROM exam_detail where exam_name=" +"'"+ json_raw['exam_name']+"';"
        cur2 = mysql.connection.cursor()
        cur2.execute(sql)
        e_id = cur2.fetchall()
        cur2.close()
        print(e_id)

        sql = "select user_id  from user_login where username ='"+json_raw['std_uname']+"';"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        u_id = cur.fetchall()
        cur.close()
        print(u_id)

        sql = "SELECT * FROM student_anwser where user_id = '"+str(u_id[0][0])+"' and exam_id = '"+str(e_id[0][0])+"';"
        print(sql)
        cur = mysql.connection.cursor()
        cur.execute(sql)
        anwsers = cur.fetchall()
        cur.close()
        print(anwsers)
        std_anwsers = []
        for i in anwsers: 
            if i[4] == None:
                std_anwsers.append({
                    'question' : i[0],
                    'anwser' : i[1],
                   
                })
            else:
                std_anwsers.append({
                    'question' : i[0],
                    'anwser' : i[1],
                    'point' : i[4]
                })
       
        return std_anwsers