from select import select
from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)
class HistoryExamination(Resource):
    def get(self):
        json_raw = request.get_json()
        sql = "SELECT * FROM point_student_exam where user_id  = "+ "'"+str(json_raw['user_name'])+"';"
        print(sql)
        cur = mysql.connection.cursor()
        cur.execute(sql)
        exams = cur.fetchall()
        cur.close()
        print(exams)
       
        all_exam = []


        for exam in exams:
            sql = "SELECT exam_name FROM exam_detail where exam_id=" +"'"+ str(exam[1])+"';"
            cur2 = mysql.connection.cursor()
            cur2.execute(sql)
            e_name = cur2.fetchall()
            cur2.close()
            print(e_name)
            
            sql = "select * from question_mcq where exam_id = '"+str(exam[1])+"';"
            print(sql)
            cur = mysql.connection.cursor()
            cur.execute(sql)
            mcq = cur.fetchall()
            print(len(mcq))

            sql = "select * from question_fitb where exam_id = '"+str(exam[1])+"';"
            print(sql)
            cur = mysql.connection.cursor()
            cur.execute(sql)
            fitb = cur.fetchall()
            print(len(fitb))

            sql = "select point from question where exam_id = '"+str(exam[1])+"'"
            cur = mysql.connection.cursor()
            cur.execute(sql)
            point_q = cur.fetchall()
            point_question = 0
            for i in point_q:
                point_question += i[0]
            
           
            all_exam.append({
                'exam' :e_name[0][0],
                'mcq' :exam[3],
                'fitb' :exam[4],
                'question' :exam[5],
                'mcq_point' : len(mcq),
                'fitb_point' : len(fitb),
                'question_point' : point_question
                
      })

        print(all_exam)

        return all_exam
