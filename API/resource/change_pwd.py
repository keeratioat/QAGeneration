from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response


app = Flask(__name__)

mysql = MySQL(app)


class ChangePwd(Resource):
    def put(self):
        json_raw = request.get_json()
        print(json_raw)

        sql = "UPDATE user_login SET password = "+"'"+json_raw['pwd_new']+"' WHERE username ='"+json_raw['uname']+"';"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()

        return {'massage' :'change_comp'}