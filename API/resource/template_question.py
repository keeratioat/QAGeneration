from select import select
from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)

class TemplateQuestion(Resource):
    def get(self):
        questions = []
        sql = "select * from template_question;"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        question = cur.fetchall()
        cur.close()

        for i in question:
             questions.append({
                'question' : i[1]
                })
        return questions