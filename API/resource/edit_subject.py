from flask import Flask,request
from flask_restful import Resource
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)


class EditSubject(Resource):
    def put(self):
        json_raw = request.get_json()
        old_sub_id = json_raw["old_sub_id"]
        sub_id = json_raw["sub_id"]
        sub_name = json_raw["sub_name"]
    
        sql = "UPDATE subject SET subject_id='"+sub_id+"'"+" , subject_name='"+sub_name+"' \
        WHERE subject_id="+"'"+old_sub_id+"'"
    
        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()
        print(sql)

        return {"Massage" : "Edit Complete"}