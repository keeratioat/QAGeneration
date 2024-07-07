from select import select
from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)

class ShowTempDetail(Resource):
    def get(self):
            teacher = request.get_json()
            print(teacher)
            sql = "SELECT user_id from user_login where username = '"+teacher['teacher']+"';"
            cur = mysql.connection.cursor()
            cur.execute(sql)
            u_id = cur.fetchall()
            cur.close()
            
                    
            sql = "select * from question_mcq where user_id = '"+str(u_id[0][0])+"';"
            print(sql)
            cur = mysql.connection.cursor()
            cur.execute(sql)
            mcq = cur.fetchall()
            print(len(mcq))

            sql = "select * from question_fitb where user_id = '"+str(u_id[0][0])+"';"
            print(sql)
            cur = mysql.connection.cursor()
            cur.execute(sql)
            fitb = cur.fetchall()
            print(len(fitb))

            sql = "select * from question where user_id = '"+str(u_id[0][0])+"';"
            print(sql)
            cur = mysql.connection.cursor()
            cur.execute(sql)
            question = cur.fetchall()
            print(len(question))
            print(question)

            total_point = 0
            question_p = 0
            for q in question:
                total_point += q[3]
                question_p += q[3]

            total_point += len(mcq)+ len(fitb)

            print(total_point)

            return {

            'mcq' : len(mcq) ,
            'fitb':len(fitb) , 
            'question' : len(question),
            'total_point' : total_point,
            'qp' : question_p
        }