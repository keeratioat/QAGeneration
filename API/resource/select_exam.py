from select import select
from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)
class SelectExam(Resource):
    def get(self):
        json_raw = request.get_json()

        sql = 'select * from student_exam where user_id  = "'+str(json_raw['user_name'])+'";'
        print(sql)
        cur = mysql.connection.cursor()
        cur.execute(sql)
        exams = cur.fetchall()
        cur.close()
       
        print(exams)

        all_exam = []

        for exam in exams:
            sql = 'select * from exam_detail where exam_id  = "'+str(exam[1])+'";'
            print(sql)
            cur = mysql.connection.cursor()
            cur.execute(sql)
            status_exam = cur.fetchall()
            cur.close()
            print(status_exam)
            if len(status_exam )> 0:
                all_exam.append({
                    'exam' :status_exam[0][1],
                    'is_exam':exam[2],
                    'status' :status_exam[0][6]
                })

        return all_exam