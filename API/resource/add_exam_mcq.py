from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
from controller.anwser_str import *
import json
app = Flask(__name__)

mysql = MySQL(app)

class AddExamMcq(Resource):
    def post(self):
        json_raw = request.get_json()

        
        count = 0
        for i in json_raw:

            sql = "SELECT user_id from user_login where username = '"+i["teacher"]+"';"
            cur = mysql.connection.cursor()
            cur.execute(sql)
            u_id = cur.fetchall()
            cur.close()
            print(i['question'])

            sql = "SELECT question_id from template_question_mcq;"
            cur = mysql.connection.cursor()
            cur.execute(sql)
            q_id = cur.fetchall()
            cur.close()
            print(i['question'])
            q_lis = []
            
            print(q_id)
            
            if str(type(i['Choice'][0])) != "<class 'int'>":
                    choice = choice_str(i['Choice'])
                    print('---------------')
                    print(len(choice))
                    print(choice)
                

                    sql = 'insert into temp_question_mcq (question,choice1,choice2,choice3,choice4,correct_anwser,user_id ,question_id)values(%s,%s,%s,%s,%s,%s,%s,%s)'             
                    print(sql, (i["question"] , choice[0] ,choice[1] ,choice[2] ,choice[3] ,correct_anwser_str(i["Correct_Ans"]) ,str(u_id[0][0]) ,q_id[count][0]))
                    cur = mysql.connection.cursor()
                    cur.execute(sql, (i["question"] , choice[0] ,choice[1] ,choice[2] ,choice[3] ,correct_anwser_str(i["Correct_Ans"]) ,str(u_id[0][0]) ,q_id[count][0]))
                    mysql.connection.commit()
                    count+=1

            else:

                    choice1  = str(i['Choice'][0])
                    choice2  = str(i['Choice'][1])
                    choice3  = str(i['Choice'][2])
                    choice4  = str(i['Choice'][3])
                    sql = 'insert into temp_question_mcq(question,choice1,choice2,choice3,choice4,correct_anwser,user_id ,question_id) values( "'+i["question"]+'","'+choice1+'","'+choice2+'", "'+choice3+'","'+choice4+'","'+str(i["Correct_Ans"])+'","'+str(u_id[0][0])+'","'+q_id[count][0]+'");'                   
                    print(sql)
                    cur = mysql.connection.cursor()
                    cur.execute(sql)
                    mysql.connection.commit()
                    print(sql)           
                    count+=1              

        return Response(response=json.dumps(json_raw))
        
    
