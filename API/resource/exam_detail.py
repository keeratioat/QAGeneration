from select import select
from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)

class ExamDetail(Resource):
    def get(self):
            exam_name = request.get_json()
            print(exam_name)
            sql = "select * from exam_detail where exam_name = '"+exam_name['exam_name']+"';"
            print(sql)
            cur = mysql.connection.cursor()
            cur.execute(sql)
            exam_detail = cur.fetchall()
            print(exam_detail)

            sql = "select * from question_mcq where exam_id = '"+str(exam_detail[0][0])+"';"
            print(sql)
            cur = mysql.connection.cursor()
            cur.execute(sql)
            mcq = cur.fetchall()
            print(len(mcq))

            sql = "select * from question_fitb where exam_id = '"+str(exam_detail[0][0])+"';"
            print(sql)
            cur = mysql.connection.cursor()
            cur.execute(sql)
            fitb = cur.fetchall()
            print(len(fitb))

            sql = "select * from question where exam_id = '"+str(exam_detail[0][0])+"';"
            print(sql)
            cur = mysql.connection.cursor()
            cur.execute(sql)
            question = cur.fetchall()
            print(len(question))
            print(question)

            total_point = 0
            for q in question:
                total_point += q[5]

            total_point += len(mcq)+ len(fitb)

            print(total_point)

            return {
            'exam_name':exam_detail[0][1],
            'exam_detail':exam_detail[0][2],
            'mcq' : len(mcq) ,
            'fitb':len(fitb) , 
            'question' : len(question),
            'hour' : exam_detail[0][3],
            'min' : exam_detail[0][4],
            'sec' : exam_detail[0][5],
            'status_exam' : exam_detail[0][6],
            'total_point' : total_point
        }