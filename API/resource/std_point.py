from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json

app = Flask(__name__)

mysql = MySQL(app)
class StdPoint(Resource):
    def get(self):
        json_raw = request.get_json()
        if(len(str(json_raw['sec']) )> 2) :
            list_of_sec =  str(json_raw['sec']).split(",")
            for i in list_of_sec:
                std_point = []

                sql = "SELECT \
                user_login.username,user_detail.firstname,user_detail.lastname \
                FROM user_login INNER JOIN user_detail ON user_login.username = user_detail.username \
                WHERE  user_detail.section = '" + i + "' AND user_login.username != '"+json_raw['uname'] +"';"
                cur = mysql.connection.cursor()
                cur.execute(sql)
                std_name = cur.fetchall()
                cur.close()
                print(std_name)


                sql = "select * from question_mcq where exam_name = '"+json_raw['exam_name']+"';"
                print(sql)
                cur = mysql.connection.cursor()
                cur.execute(sql)
                mcq = cur.fetchall()
                print(len(mcq))

                sql = "select * from question_fitb where exam_name = '"+json_raw['exam_name']+"';"
                print(sql)
                cur = mysql.connection.cursor()
                cur.execute(sql)
                fitb = cur.fetchall()
                print(len(fitb))

                sql = "select point from question where exam_name = '"+json_raw['exam_name']+"'"
                cur = mysql.connection.cursor()
                cur.execute(sql)
                point_q = cur.fetchall()
                point_question = 0
                for i in point_q:
                    point_question += i[0]

                if(len(std_name) > 0):
                    for i in std_name:
                        sql = "SELECT * FROM point_student_exam WHERE student =" +"'" +i[0]+"' AND exam_name = '" + json_raw['exam_name'] +"';"
                        print(sql)
                        cur = mysql.connection.cursor()
                        cur.execute(sql)
                        exam_point = cur.fetchall()
                        cur.close()

                        print(exam_point)

                

                        for j in exam_point:
                            std_point.append({
                            'student_id' : i[0],
                            'firstname' : i[1],
                            'lastname' :i[2],
                            'mcq':j[2],
                            'fitb':j[3],
                            'question':j[4],
                            'mcq_point' : len(mcq),
                            'fitb_point' : len(fitb),
                            'question_point' : point_question

                            })

                print(std_point)

                return std_point
                

        else:
            std_point = []

            sql = "SELECT \
                user_login.username,user_detail.firstname,user_detail.lastname \
                FROM user_login INNER JOIN user_detail ON user_login.user_id = user_detail.user_id \
                WHERE  user_detail.section = '" + str(json_raw['sec']) + "' AND user_login.username != '"+json_raw['uname'] +"';"
            cur = mysql.connection.cursor()
            cur.execute(sql)
            std_name = cur.fetchall()
            cur.close()
            print(std_name)

            sql = "SELECT exam_id FROM exam_detail where exam_name=" +"'"+ json_raw['exam_name']+"';"
            cur2 = mysql.connection.cursor()
            cur2.execute(sql)
            e_id = cur2.fetchall()
            cur2.close()
            print(e_id)

            sql = "select * from question_mcq where exam_id = '"+str(e_id[0][0])+"';"
            print(sql)
            cur = mysql.connection.cursor()
            cur.execute(sql)
            mcq = cur.fetchall()
            print(len(mcq))

            sql = "select * from question_fitb where exam_id = '"+str(e_id[0][0])+"';"
            print(sql)
            cur = mysql.connection.cursor()
            cur.execute(sql)
            fitb = cur.fetchall()
            print(len(fitb))

            sql = "select point from question where exam_id = '"+str(e_id[0][0])+"'"
            cur = mysql.connection.cursor()
            cur.execute(sql)
            point_q = cur.fetchall()
            point_question = 0
            for i in point_q:
                point_question += i[0]

            if(len(std_name) > 0):
                for i in std_name:
                    sql = "select user_id  from user_login where username ='"+i[0]+"';"
                    cur = mysql.connection.cursor()
                    cur.execute(sql)
                    u_id = cur.fetchall()
                    cur.close()
                    print(u_id)

                    sql = "SELECT * FROM point_student_exam WHERE user_id =" +"'" +str(u_id[0][0])+"' AND exam_id = '" + str(e_id[0][0]) +"';"
                    print(sql)
                    cur = mysql.connection.cursor()
                    cur.execute(sql)
                    exam_point = cur.fetchall()
                    cur.close()

                    print(exam_point)

                

                    for j in exam_point:
                        print(j)
                        std_point.append({
                            'student_id' : i[0],
                            'firstname' : i[1],
                            'lastname' :i[2],
                            'mcq':j[3],
                            'fitb':j[4],
                            'question':j[5],
                            'mcq_point' : len(mcq),
                            'fitb_point' : len(fitb),
                            'question_point' : point_question

                            })

            print(std_point)

            return std_point