from flask import Flask,Response
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)

class TempQuestionExamFitb(Resource):
    def get(self):

        sql = 'SELECT * FROM temp_question_fitb'
        cur = mysql.connection.cursor()
        cur.execute(sql)
        questions = cur.fetchall()
        cur.close()
        fitb_question = []

        for question in questions:
            fitb_question.append({
                'question' :question[2], 
                'anwser' : question[4]
                })
        
        return Response(response=json.dumps(fitb_question))