from flask import Flask,request
from flask_restful import Resource
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)


class ChangeExamStatusClose(Resource):
    def put(self):
        json_raw = request.get_json()
        print(json_raw)

        
            
        sql = "UPDATE exam_detail SET status_exam = 'close' WHERE user_id = %s AND exam_name = %s;"
        print(sql)
        cur = mysql.connection.cursor()
        cur.execute(sql,(json_raw['teacher'],json_raw['exam_name']))
        mysql.connection.commit()

       
