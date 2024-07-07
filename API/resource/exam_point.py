from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json
app = Flask(__name__)

mysql = MySQL(app)

class ExamPoint(Resource):
    def post(self):
        json_raw = request.get_json()
        print(json_raw)
        
        sql = "SELECT exam_id FROM exam_detail where exam_name=" +"'"+ json_raw['exam_name']+"';"
        cur2 = mysql.connection.cursor()
        cur2.execute(sql)
        e_id = cur2.fetchall()
        cur2.close()
        print(e_id)

        sql = "INSERT INTO point_student_exam (user_id , exam_id ,mcq_point ,fitb_point)VALUES("+"'"+str(json_raw['student'])+"','"+str(e_id[0][0])+"',"+str(json_raw['mcq'])+","+str(json_raw['fitb'])+');'
        
        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()
