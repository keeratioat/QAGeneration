from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response


app = Flask(__name__)

mysql = MySQL(app)


class EditTotalPointQuestion(Resource):
    def put(self):
        json_raw = request.get_json()
        total_point = json_raw['total_point_quetion']
        student = json_raw['student']
        exam_name = json_raw['exam_name']

        sql = "select user_id  from user_login where username ='"+student+"';"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        u_id = cur.fetchall()
        cur.close()
        print(u_id)


        sql = "SELECT exam_id FROM exam_detail where exam_name=" +"'"+exam_name+"';"
        cur2 = mysql.connection.cursor()
        cur2.execute(sql)
        e_id = cur2.fetchall()
        cur2.close()
        print(e_id)

        sql = "UPDATE point_student_exam SET question_point = " + str(total_point) + " WHERE exam_id = '" +str(e_id[0][0]) +"' AND user_id = '" + str(u_id[0][0]) +"';"
        print(sql)

        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()
        print(sql)

        print(json_raw)