from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)

class ShowAllExam(Resource):
    def get(self):
        json_raw = request.get_json()
        print(json_raw)

        sql = 'SELECT * FROM exam_detail WHERE user_id ='+"'"+str(json_raw['teacher'])+"';"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        all_exam = cur.fetchall()
        print(all_exam)
        exam = []
        for ex in all_exam:
            exam.append({
                'exam_id' : ex[0],
                'exam_name' : ex[1],
                'status' : ex[6]
            })

        print(exam)

        return exam