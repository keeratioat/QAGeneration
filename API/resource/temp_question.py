from flask import Flask,Response
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)

class TempQuestionExam(Resource):
    def get(self):
    
        sql = 'SELECT * FROM temp_question'
        cur = mysql.connection.cursor()
        cur.execute(sql)
        questions = cur.fetchall()
        cur.close()
        mcq_question = []

        for question in questions:
            mcq_question.append({
                'question' :question[2],
                
                })

        return Response(response=json.dumps(mcq_question))