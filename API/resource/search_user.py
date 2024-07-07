from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)

class SearchUser(Resource):
    def post(self):
        json_raw = request.get_json()
        search = json_raw["search"]
        print(search)
        sql = "SELECT user_login.username,user_detail.firstname ,user_detail.lastname,\
         user_detail.subject_name ,user_detail.username,user_detail.section ,\
         user_login.status \
            FROM user_login \
            INNER JOIN user_detail ON user_login.username = user_detail.username\
            WHERE user_detail.firstname = "+"'"+search+"' OR user_detail.lastname = "+"'"+search+"'" + " OR user_login.username = " +"'"+search+"'"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        user = cur.fetchall()
        userlist = []
        for u in user:
            userlist.append({
            'std_id' :u[0],
            'firstname' : u[1],
            'lastname': u[2],
            'subject': u[3],
            'user_id' :u[4],
            'section' :u[5],
            'status' :u[6],
            
            
        })
        return Response(response=json.dumps(userlist))