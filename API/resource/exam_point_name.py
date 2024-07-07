from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)
class ExamPointName(Resource):
    def get(self):
       
        json_raw = request.get_json()
        print(json_raw)

        sql = 'SELECT * FROM exam_detail WHERE user_id ='+"'"+str(json_raw['uname'])+"';"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        all_exam = cur.fetchall()
        print(all_exam)
        exam = []
        for ex in all_exam:
            exam.append({
                'exam_name' : ex[1],
                'status' : ex[6]
            })

        print(exam)

        return exam