from flask import Flask,Response
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)


class Index(Resource):
    def get(self):
        sql = "SELECT user_detail.firstname,user_detail.lastname,user_login.username,\
        user_login.status \
            FROM user_login \
                INNER JOIN user_detail ON user_login.user_id = user_detail.user_id \
                    WHERE user_login.username = 'keerati' AND user_login.password = 'e10adc3949ba59abbe56e057f20f883e'"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        user = cur.fetchall()
        cur.close()
        userList = []
        for u in user:
            userList.append({
            'firstname' : u[0],
            'lastname': u[1],
            'username': u[2],
            'status': u[3]
        })
        return Response(response=json.dumps(userList))


