from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)

class ExamInfo(Resource):
    def get(self):
        exam_info = []
        json_raw = request.get_json()
        sql = "select exam_name from exam_detail where teacher = '"+json_raw['teacher']+"';"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        t_name = cur.fetchall()
        cur.close()
        len_t_name =len(t_name)
        print(len_t_name)
        if(len (t_name) > 0):
            print(t_name[0][0])
            for i in range(len_t_name):
                print(i)

                sql = "select * from student_exam where exam_name = '"+t_name[i][0]+"';"
                print(sql)
                cur = mysql.connection.cursor()
                cur.execute(sql)
                exam_name = cur.fetchall()
                cur.close()
            

                for en in exam_name:
                    exam_info.append({
                    'exam_name': en[1],
                    'firstname': en[2],
                    'lastname': en[3]

                    })

        return exam_info