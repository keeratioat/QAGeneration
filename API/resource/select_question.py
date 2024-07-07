from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
from requests import delete


app = Flask(__name__)

mysql = MySQL(app)


class SelectQuestion(Resource):
    def post(self):
        json_raw = request.get_json()
        sql  = "delete from question where exam_id is null"
        print(sql)
        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()

        sql  = "delete from question_mcq where exam_id is null"
        print(sql)
        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()

        sql  = "delete from question_fitb where exam_id is null"
        print(sql)
        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()

        
        for i in json_raw:
            print(i["teacher"])
            sql = "SELECT user_id from user_login where username = '"+i["teacher"]+"';"
            cur = mysql.connection.cursor()
            cur.execute(sql)
            u_id = cur.fetchall()
            cur.close()
            print(i['question'])
            
            sql = "SELECT * FROM temp_question WHERE question = '"+i['question']+"';"
            
            cur = mysql.connection.cursor()
            cur.execute(sql)
            questions = cur.fetchall()
            cur.close()
            question = []
            for q in questions:
                question.append({
                    'question_id' :q[1],
                    'question' :q[2],
                    
                    })
            
            if(len(question) == 1):
                sql = "insert into question(question,user_id,question_id) values("+"'"+question[0]['question']+"','"+str(u_id[0][0])+"','"+question[0]['question_id']+"');"
                print(sql)
                print('----------------')
                cur = mysql.connection.cursor()
                cur.execute(sql)
                mysql.connection.commit()
               
                
            
            sql = "SELECT * FROM temp_question_mcq WHERE question = '"+i['question']+"';"
            cur = mysql.connection.cursor()
            cur.execute(sql)
            questions = cur.fetchall()
            cur.close()
            print(question)
            print("----")
            print(questions)
            print("----")

            mcq_question = []
            for q in questions:
                mcq_question.append({
                    'question_id':q[1],
                    'question' :q[2],
                    'choice1' : q[4],
                    'choice2' : q[5],
                    'choice3' : q[6],
                    'choice4' : q[7],
                    'answer' : q[8],
                    'teacher' :q[1]
                    })
            if(len(mcq_question) == 1):
                sql2 = 'insert into question_mcq(question,choice1,choice2,choice3,choice4,anwser,user_id,question_id) values('+'"'+\
                    mcq_question[0]["question"]+'","'+mcq_question[0]['choice1']+'","'+mcq_question[0]['choice2']+'","'+\
                        mcq_question[0]['choice3']+'","'+mcq_question[0]['choice4']+'","'+mcq_question[0]['answer']+'","'+str(u_id[0][0])+'","'+mcq_question[0]['question_id']+'");'
                print(sql2)
                print('----------------')
                cur2 = mysql.connection.cursor()
                cur2.execute(sql2)
                mysql.connection.commit()

            sql = "SELECT * FROM temp_question_fitb WHERE question = '"+i['question']+"';"
            
            print(sql)
            cur = mysql.connection.cursor()
            cur.execute(sql)
            questions = cur.fetchall()
            cur.close()
            fitb_question = []
            print(questions)
            for q in questions:
                fitb_question.append({
                    'question_id': q[1],
                   'question' :q[2],
                   'answer' : q[4],
                    'teacher' : q[3]
                    })
            print(fitb_question)
            if(len(fitb_question) == 1):
                sql3 = "insert into question_fitb(question,anwser,user_id,question_id) values("+"'"+fitb_question[0]['question']+"','"+fitb_question[0]['answer']+"','"+str(u_id[0][0])+"','"+fitb_question[0]['question_id']+"');"
                cur3 = mysql.connection.cursor()
                cur3.execute(sql3)
                mysql.connection.commit()                



    def delete(self):


        sql = "delete from temp_question;" 
        cur= mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit() 

        sql = "delete from temp_question_fitb;" 
        cur= mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit() 

        sql = "delete from temp_question_mcq;" 
        cur= mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit() 
      
    def put(self):
        json_raw = request.get_json()

        print(json_raw)
        for i in json_raw:
            sql = "UPDATE question SET point = "+""+i['point']+" WHERE question ='"+i['question']+"'" + "AND exam_id is null;"
            print(sql)
            cur = mysql.connection.cursor()
            cur.execute(sql)
            mysql.connection.commit()