from flask import Flask
from flask_restful import Resource
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)

class DeleteTempExam(Resource):
    def delete(self):

        sql2 = "delete from temp_question;"
        cur = mysql.connection.cursor()
        cur.execute(sql2)
        mysql.connection.commit()
        cur.close()

        sql3 = "delete from temp_question_fitb;"
        cur = mysql.connection.cursor()
        cur.execute(sql3)
        mysql.connection.commit()
        cur.close()

        sql4 = "delete from temp_question_mcq;"
        cur = mysql.connection.cursor()
        cur.execute(sql4)
        mysql.connection.commit()
        cur.close()

        return {"Massage" : "Delete Complete"}