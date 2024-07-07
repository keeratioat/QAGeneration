from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response

app = Flask(__name__)

mysql = MySQL(app)

class AddExamDetail(Resource):
    def post(self):
        exam_detail = request.get_json()
        
        print(exam_detail)
        sql = "insert into exam_detail(exam_name,exam_detail,hour,min,sec,user_id,status_exam) values("+"'"+exam_detail['exam_name']+"','"+exam_detail['exam_detail']+"','"+\
            str(exam_detail['hr'])+"','"+str(exam_detail['min'])+"','"+str(exam_detail['sec'])+"','"+str(exam_detail['teacher'])+"','close');"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()

        sql = "SELECT exam_id FROM exam_detail where exam_name=" +"'"+ exam_detail['exam_name']+"';"
        cur2 = mysql.connection.cursor()
        cur2.execute(sql)
        e_id = cur2.fetchall()
        cur2.close()
        print(e_id)
        if(len(str(exam_detail['section']) )> 2) :
            list_of_sec =  str(exam_detail['section']).split(",")
            print(list_of_sec)
            for i in list_of_sec:
                sql2 = "SELECT user_login.user_id ,user_detail.firstname,user_detail.lastname\
                FROM user_login \
                    INNER JOIN user_detail ON user_login.user_id = user_detail.username_id \
                        WHERE user_login.user_id !=  "+"'"+exam_detail['teacher']+"'"+ " AND user_detail.subject_name =" +"'"+\
                            exam_detail['subject_name']+"' AND user_detail.section = '"+i+"';"
        
                cur2 = mysql.connection.cursor()
                cur2.execute(sql2)
                user = cur2.fetchall()
                cur2.close()
                print(user)

                
        
                for u in user:
                    sql3 = "INSERT INTO student_exam (user_id,exam_id,firstname,lastname) VALUES("+"'"+u[0]+"','"+e_id[0][0]+"','"+u[1]+"','"+u[2]+"');"
                    print(sql3)
                    cur3 = mysql.connection.cursor()
                    cur3.execute(sql3)
                    mysql.connection.commit()

                    sql4 = "UPDATE question SET exam_id = "+"'"+e_id[0][0]+"'"+ "WHERE exam_name is NULL;"
                    print(sql4)
                    cur4 = mysql.connection.cursor()
                    cur4.execute(sql4)
                    mysql.connection.commit()

                    sql5 = "UPDATE question_mcq SET exam_id = "+"'"+e_id[0][0]+"'"+ "WHERE exam_name is NULL;"
                    print(sql5)
                    cur4 = mysql.connection.cursor()
                    cur4.execute(sql5)
                    mysql.connection.commit()

                    sql6 = "UPDATE question_fitb SET exam_id = "+"'"+e_id[0][0]+"'"+ "WHERE exam_name is NULL;"
                    print(sql6)
                    cur4 = mysql.connection.cursor()
                    cur4.execute(sql6)
                    mysql.connection.commit()

                    sql7 = "UPDATE file_java SET exam_id = "+"'"+e_id[0][0]+"'"+ "WHERE exam_name is NULL;"
                    print(sql7)
                    cur4 = mysql.connection.cursor()
                    cur4.execute(sql7)
                    mysql.connection.commit()

        else:
            sql2 = "SELECT user_login.user_id ,user_detail.firstname,user_detail.lastname\
                FROM user_login \
                    INNER JOIN user_detail ON user_login.user_id = user_detail.user_id \
                        WHERE user_login.user_id !=  "+"'"+str(exam_detail['teacher'])+"'"+ " AND user_detail.subject_name =" +"'"+\
                            exam_detail['subject_name']+"' AND user_detail.section = '"+str(exam_detail['section'])+"';"
        
            cur2 = mysql.connection.cursor()
            cur2.execute(sql2)
            user = cur2.fetchall()
            cur2.close()
            print(user)
        
            for u in user:
                sql3 = "INSERT INTO student_exam (user_id,exam_id) VALUES("+"'"+str(u[0])+"','"+str(e_id[0][0])+"');"
                print(sql3)
                cur3 = mysql.connection.cursor()
                cur3.execute(sql3)
                mysql.connection.commit()

                sql4 = "UPDATE question SET exam_id = "+"'"+str(e_id[0][0])+"'"+ "WHERE exam_id is NULL;"
                print(sql4)
                cur4 = mysql.connection.cursor()
                cur4.execute(sql4)
                mysql.connection.commit()

                sql5 = "UPDATE question_mcq SET exam_id = "+"'"+str(e_id[0][0])+"'"+ "WHERE exam_id is NULL;"
                print(sql5)
                cur4 = mysql.connection.cursor()
                cur4.execute(sql5)
                mysql.connection.commit()

                sql6 = "UPDATE question_fitb SET exam_id = "+"'"+str(e_id[0][0])+"'"+ "WHERE exam_id is NULL;"
                print(sql6)
                cur4 = mysql.connection.cursor()
                cur4.execute(sql6)
                mysql.connection.commit()

                sql7 = "UPDATE file_java SET exam_id = "+"'"+str(e_id[0][0])+"'"+ "WHERE exam_id is NULL;"
                print(sql7)
                cur4 = mysql.connection.cursor()
                cur4.execute(sql7)
                mysql.connection.commit()


