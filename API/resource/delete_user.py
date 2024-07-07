from flask import Flask
from flask_restful import Resource
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)

class DeleteUser(Resource):
    def delete(self,id):
        print(id)
        sql = "SELECT user_id FROM user_login WHERE username ='"+id+"';"
        
        cur = mysql.connection.cursor()
        cur.execute(sql)
        std = cur.fetchall()
        cur.close()
        print("------------")
        print(std[0][0])
        print("------------")
        sql = "DELETE FROM user_detail WHERE user_id = "+"'"+str(std[0][0])+"'"
        sql2 = "DELETE FROM user_login WHERE username = "+"'"+id+"'"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()
        cur.execute(sql2)
        mysql.connection.commit()
        cur.close()
        return  {"Massage":"Delete complete"}