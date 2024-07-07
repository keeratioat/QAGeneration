from flask import Flask
from flask_restful import Resource
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)

class DeleteSubject(Resource):
    def delete(self,id):
        print(id)
        sql = "DELETE FROM subject WHERE subject_id = "+"'"+id+"'"
        print(sql)
        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()
        cur.close()
