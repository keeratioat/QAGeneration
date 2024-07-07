from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)

class GetTeacherNameStd(Resource):
    def get(self):
        json = json_raw = request.get_json()
        print(json)

        sql = "SELECT exam_name FROM student_exam WHERE student = '"+json['std_name']+"';"
        print(sql)
        cur = mysql.connection.cursor()
        cur.execute(sql)
        exam_name = cur.fetchall()
        
        print(exam_name[0][0])

        sql = "SELECT teacher FROM exam_detail WHERE exam_name = '"+exam_name[0][0]+"';"
        print(sql)
        cur = mysql.connection.cursor()
        cur.execute(sql)
        teacher_name = cur.fetchall()
        print(teacher_name[0][0])

        return{'teacher_name':teacher_name[0][0]}