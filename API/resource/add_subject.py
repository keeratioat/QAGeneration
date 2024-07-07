from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response


app = Flask(__name__)

mysql = MySQL(app)


class AddSubject(Resource):
    def post(self):
        json_raw = request.get_json()
        sub_id = json_raw["sub_id"]
        sub_name = json_raw["sub_name"]
        sql = "insert into subject values("+"'"+sub_id+"','"+sub_name+"');"
        print(sql)
        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()
        return {"Massage":"Add Complete"}