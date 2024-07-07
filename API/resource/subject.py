from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response

from flask_mysqldb import MySQL
import json

app = Flask(__name__)

mysql = MySQL(app)

class Subject(Resource):
    def get(self):
        sql = "select * from subject"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        user = cur.fetchall()
        cur.close()
        subjectlist = []
        for u in user:
            subjectlist.append({
            'subject_id' : u[0],
            'subject_name': u[1],
        })
        return Response(response=json.dumps(subjectlist))