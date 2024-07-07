from flask import Flask
from flask_restful import Resource
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)
class DeleteExam(Resource):
    def delete(self,exam_name):

        sql = "SELECT exam_id FROM exam_detail where exam_name=" +"'"+ exam_name+"';"
        cur2 = mysql.connection.cursor()
        cur2.execute(sql)
        e_id = cur2.fetchall()
        cur2.close()
        print(e_id)

        sql2 = "delete from exam_detail where exam_id = '"+str(e_id[0][0])+"';"
        sql3 = "delete from question where exam_id = '"+str(e_id[0][0])+"';"
        sql4 = "delete from question_fitb where exam_id = '"+str(e_id[0][0])+"';"
        sql5 = "delete from question_mcq where exam_id = '"+str(e_id[0][0])+"';"
        sql6 = "delete from student_exam where exam_id = '"+str(e_id[0][0])+"';"
        sql7 = "delete from file_java where exam_id = '"+str(e_id[0][0])+"';"
        sql8 = "delete from point_student_exam where exam_id = '"+str(e_id[0][0])+"';"
        sql9 = "delete from student_anwser where exam_id = '"+str(e_id[0][0])+"';"
        

        print(sql2)
        print(sql3)
        print(sql4)
        print(sql5)
        print(sql6)
        print(sql7)

        cur = mysql.connection.cursor()

        
        cur.execute(sql3)
        mysql.connection.commit()
        cur.execute(sql4)
        mysql.connection.commit()
        cur.execute(sql5)
        mysql.connection.commit()
        cur.execute(sql6)
        mysql.connection.commit()
        cur.execute(sql7)
        mysql.connection.commit()
        cur.execute(sql8)
        mysql.connection.commit()
        cur.execute(sql9)
        mysql.connection.commit()
        cur.execute(sql2)
        mysql.connection.commit()
        cur.close()

        
        return {"Massage":"Delete exam complete"}
