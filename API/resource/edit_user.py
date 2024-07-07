from flask import Flask,request
from flask_restful import Resource
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)
class EditUser(Resource):
    def put(self):
        json_raw = request.get_json()
        name = json_raw['name']
        lastname = json_raw['lastname']
        status = json_raw['status']
        sub_name = json_raw['sub_name']
        section = json_raw['section']
        old_name = json_raw['old_name']
        old_lastname = json_raw['old_lastname']

        print(name , " " ,lastname ," " ,status , " " ,sub_name , " " ,section ," " ,old_name , " ",old_lastname)

        sql = "UPDATE user_login l INNER JOIN user_detail d on l.user_id = d.user_id SET d.firstname = "+"'"+name+"',"\
            +"d.lastname ='"+lastname+"', l.status ='"+status+"', d.subject_name = '"+ sub_name+"',d.section = '"+section+"' WHERE "\
                +"d.firstname ='"+old_name+"'and d.lastname = '"+old_lastname+"'"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()

        return {"Massage" : "Edit Complete"}