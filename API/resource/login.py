from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)

class Login(Resource):
    def post(self):
        json_raw = request.get_json()
        uname = json_raw["user_name"]
        password = json_raw["password"]
        print(uname," ",password)
        sql = "SELECT user_detail.firstname ,user_detail.lastname,user_detail.section\
             ,user_login.username \
        ,user_login.status , user_detail.subject_name,user_login.user_id \
            FROM user_login \
                INNER JOIN user_detail ON user_login.user_id = user_detail.user_id \
                    WHERE user_login.username =  "+"'"+uname+"'"+ " AND user_login.password =" +"'"+password+"'";
        print(sql)
        cur = mysql.connection.cursor()
        cur.execute(sql)
        user = cur.fetchall()
        cur.close()
        print(user)
        userList = []
        for u in user:
            userList.append({
            'firstname' : u[0],
            'lastname': u[1],
            'section': u[2],
            'username': u[3],
            'status': u[4],
            'subject_name' : u[5],
            'user_id' : u[6]
       })
        return Response(response=json.dumps(userList))