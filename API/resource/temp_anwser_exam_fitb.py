from flask import Flask,Response
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)

class TempAnwserExamFitb(Resource):
    def get(self):

        sql = 'SELECT * FROM temp_all_anwser_fitb'
        cur = mysql.connection.cursor()
        cur.execute(sql)
        anwsers = cur.fetchall()
        cur.close()
        fitb_anwsers = []

        for anwser in anwsers:
            fitb_anwsers.append({
                'anwser' :anwser[0], 
                })
        
        return Response(response=json.dumps(fitb_anwsers))