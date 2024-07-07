from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json
app = Flask(__name__)

mysql = MySQL(app)

class StudentAnwser(Resource):
    def post(self):
        json_raw = request.get_json()
        print(json_raw)

        sql = "SELECT exam_id FROM exam_detail where exam_name=" +"'"+ json_raw['exam_name']+"';"
        cur2 = mysql.connection.cursor()
        cur2.execute(sql)
        e_id = cur2.fetchall()
        cur2.close()
        print(e_id)

        sql = "INSERT INTO student_anwser(question,anwser,exam_id,user_id) VALUES("+"'"+\
            json_raw['question']+"','"+json_raw['anwser']+"','"+str(e_id[0][0])+"','"+json_raw['student']+"');"
        print(sql)
        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()
    
    def get(self):
        std = []
        json_raw = request.get_json()
        
        sql = "SELECT exam_id FROM exam_detail where exam_name=" +"'"+ json_raw['exam_name']+"';"
        cur2 = mysql.connection.cursor()
        cur2.execute(sql)
        e_id = cur2.fetchall()
        cur2.close()
        print(e_id)

        exam_n = []
        sql = "select exam_id from exam_detail where user_id = '"+str(json_raw['teacher'])+"' and exam_id = '"+str(e_id[0][0])+"';"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        t_name = cur.fetchall()
        cur.close()
        print(t_name)

       
        len_t_name =len(t_name)
        

        if(len (t_name) > 0):
            for i in range(len_t_name):
               
                print(t_name[i])
                          
                sql = "select * from point_student_exam where exam_id ='"+str(t_name[i][0])+"';"
                cur = mysql.connection.cursor()
                cur.execute(sql)
                exams = cur.fetchall()
                cur.close()
                print('--------------')
                print(i)
                print(exams)
                print('--------------')
                if(len(exams) > 0):    
                   
                        for j in range(len(exams)):
                             
                           
                                print(exams[j])
                            
                                sql = "select * from student_exam where user_id = '"+str(exams[j][0])+"' and exam_id ='"+str(exams[j][1])+"';"
                                cur = mysql.connection.cursor()
                                cur.execute(sql)
                                exam_name = cur.fetchall()
                                cur.close()
                            
                                print(exam_name)

                                sql = "select firstname , lastname from user_detail where user_id ='"+str(exams[j][0])+"';"
                                cur = mysql.connection.cursor()
                                cur.execute(sql)
                                user = cur.fetchall()
                                cur.close()
                                print(user)

                                sql = "select username  from user_login where user_id ='"+str(exams[j][0])+"';"
                                cur = mysql.connection.cursor()
                                cur.execute(sql)
                                username = cur.fetchall()
                                cur.close()
                                print(user)

                                

                                print(exams)

                                for en in exam_name:

                                    sql = "select username  from user_login where user_id ='"+str(en[0])+"';"
                                    cur = mysql.connection.cursor()
                                    cur.execute(sql)
                                    username = cur.fetchall()
                                    cur.close()
                                    print(user)

                                    sql = "select exam_name  from exam_detail where exam_id ='"+str(en[1])+"';"
                                    cur = mysql.connection.cursor()
                                    cur.execute(sql)
                                    ex_name = cur.fetchall()
                                    cur.close()
                                    print(ex_name)

                                    
                                    std.append({
                                        'uname':username[0][0],
                                        'exam_name': ex_name[0][0],
                                        'firstname': user[0][0],
                                        'lastname': user[0][1],
                                        'status' : exams[0][4],
                                        'is_check' : exams[j][5]

                         })

                        print(std)
                

        return sorted(std , key=lambda i: i['uname'] )

    def put(self):
        json_raw = request.get_json()
        sql = "SELECT exam_id FROM exam_detail where exam_name=" +"'"+ json_raw['exam_name']+"';"
        cur2 = mysql.connection.cursor()
        cur2.execute(sql)
        e_id = cur2.fetchall()
        cur2.close()
        print(e_id)

        sql = "UPDATE student_exam SET is_exam = 1 WHERE user_id = "+ "'"+json_raw['student'] +"' AND exam_id ='"+str(e_id[0][0])+"';"
        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()
        
        print(json_raw)