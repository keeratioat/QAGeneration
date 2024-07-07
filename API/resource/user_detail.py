from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)

class UserDetail(Resource):
    def get(self):
        sql = "SELECT user_detail.firstname ,user_detail.lastname,\
         user_detail.subject_name ,user_detail.user_id,user_detail.section ,\
         user_login.status \
         FROM user_login INNER JOIN user_detail ON user_login.user_id = user_detail.user_id"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        user = cur.fetchall()
        cur.close()
        userlist = []
        for u in user:
            userlist.append({
            'firstname' : u[0],
            'lastname': u[1],
            'subject': u[2],
            'user_id' :u[3],
            'section' :u[4],
            'status' :u[5],
            
            })
        return Response(response=json.dumps(userlist))