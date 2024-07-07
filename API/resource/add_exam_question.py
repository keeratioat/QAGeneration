from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response


app = Flask(__name__)

mysql = MySQL(app)


class AddQuestionExam(Resource):
    def post(self):
        json_raw = request.get_json()
        count = 0
        for i in json_raw:

            sql = "SELECT user_id from user_login where username = '"+i["teacher"]+"';"
            cur = mysql.connection.cursor()
            cur.execute(sql)
            u_id = cur.fetchall()
            cur.close()
            print(i['question'])

            sql = "SELECT question_id from template_question;"
            cur = mysql.connection.cursor()
            cur.execute(sql)
            q_id = cur.fetchall()
            cur.close()

            sql = "insert into temp_question (question  ,user_id,question_id) values("+"'"+i['question']+"','"+str(u_id[0][0])+"','"+q_id[count][0]+"');"
            cur = mysql.connection.cursor()
            cur.execute(sql)
            mysql.connection.commit()
            count+=1