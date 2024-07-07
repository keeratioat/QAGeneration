from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response


app = Flask(__name__)

mysql = MySQL(app)


class AddUser(Resource):
    def post(self):
        json_raw = request.get_json()
        name = json_raw["name"]
        lastname = json_raw["lastname"]
        username = json_raw["username"]
        pwd = json_raw["pwd"]
        status = json_raw["status"]
        sub_name = json_raw["sub_name"]
        section = json_raw["section"]

        print(name + " " +lastname +" "+pwd + " "+status + " "+sub_name + " "+str(section))
    
        try:
            sql = "INSERT INTO user_login (username , password , status) VALUES( "+"'"+username+"',"+"'"+pwd+"',"+"'"+status+"')"
            cur = mysql.connection.cursor()
            cur.execute(sql)
            mysql.connection.commit()

    
            sql2 = "INSERT INTO user_detail (firstname , lastname , user_id, subject_name, section) \
            SELECT "+"'"+ name+"'," +"'"+lastname+"', user_id" +",'"+sub_name+"','"+str(section)+"' FROM user_login WHERE username = '"+username+"'"
            cur2 = mysql.connection.cursor()
            cur2.execute(sql2)
            mysql.connection.commit()

            print(sql2)
            return {"Massage":"Add Complete"}
        except:
            return {"Massage":"Have user in DB"}