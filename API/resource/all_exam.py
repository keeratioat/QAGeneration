from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)

class AllExam(Resource):
    def get(self):
        exam_name_json = request.get_json()
        print(exam_name_json)

        sql = "SELECT exam_id FROM exam_detail where exam_name=" +"'"+ exam_name_json['exam_name']+"';"
        cur2 = mysql.connection.cursor()
        cur2.execute(sql)
        e_id = cur2.fetchall()
        cur2.close()
        print(e_id)

        sql = 'SELECT * FROM question_mcq WHERE exam_id ='+"'"+str(e_id[0][0])+"';"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        all_exam = cur.fetchall()
        print(all_exam)
        exams = []
        for exam in all_exam:
            exams.append({
                'question' :exam[2],
                'choice1':  exam[5],
                'choice2':  exam[6],
                'choice3' : exam[7],
                'choice4' : exam[8],
                'correct_choice':exam[9],
                'exam_type' : 'mcq'
            })

        sql = 'SELECT * FROM question WHERE exam_id ='+"'"+str(e_id[0][0])+"';"    
        cur = mysql.connection.cursor()
        cur.execute(sql)
        all_exam = cur.fetchall()
        print('------------------------')
        print(all_exam)

        for exam in all_exam:
            exams.append({
                'question' :exam[2] +" (" +str(exam[5])+" คะแนน)",
                'exam_type' : 'question'
            })

        sql = 'SELECT * FROM question_fitb WHERE exam_id ='+"'"+str(e_id[0][0])+"';"    
        cur = mysql.connection.cursor()
        cur.execute(sql)
        all_exam = cur.fetchall()
        print('------------------------')
        print(all_exam)

        for exam in all_exam:
            exams.append({
                'question' :exam[2],
                'all_anwser' : exam[5],
                'exam_type' : 'fitb'
            })

        return exams