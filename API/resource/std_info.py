from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)
class StdInfo(Resource):
    def get(self):
        all_std = []
        json_raw = request.get_json()
        if(len(str(json_raw['section']) )> 2) :
            list_of_sec =  str(json_raw['section']).split(",")
            print(list_of_sec)
            for i in list_of_sec:
                sql = "SELECT user_login.username,user_detail.firstname ,user_detail.lastname,\
            user_detail.subject_name ,user_login.username,user_detail.section ,\
            user_login.status \
            FROM user_login INNER JOIN user_detail ON user_login.user_id = user_detail.user_id WHERE \
            user_detail.section = '"+i+"' \
            and user_login.status = 'student' ORDER BY user_login.username ASC;"

                cur = mysql.connection.cursor()
                cur.execute(sql)
                std = cur.fetchall()
                cur.close()
                print(std)
                
                for u in std:
                    all_std.append({
                'std_id' : u[0],
                'firstname' : u[1],
            'lastname': u[2],
            'subject': u[3],
            'user_id' :u[4],
            'section' :u[5],
            'status' :u[6],
            })

            return all_std
           
        

        #sql = "SELECT * FROM user_detail where subject_name  = "+ "'"+json_raw['subject']+"' and section = "+ str(json_raw['section']) \
           # +" and firstname != '"+json_raw['first_name']+"' and lastname !='"+json_raw['lastname']+"';"
        else:
            sql = "SELECT user_login.username,user_detail.firstname ,user_detail.lastname,\
            user_detail.subject_name ,user_login.username,user_detail.section ,\
            user_login.status \
            FROM user_login INNER JOIN user_detail ON user_login.user_id = user_detail.user_id WHERE \
            user_detail.section = '"+str(json_raw['section'])+"' \
            and user_login.status = 'student' ORDER BY user_login.username ASC;"

            cur = mysql.connection.cursor()
            cur.execute(sql)
            std = cur.fetchall()
            cur.close()
            print(std)
            all_std = []
            for u in std:
                all_std.append({
                'std_id' : u[0],
                'firstname' : u[1],
            'lastname': u[2],
            'subject': u[3],
            'user_id' :u[4],
            'section' :u[5],
            'status' :u[6],
            })

            return all_std