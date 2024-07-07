from flask import Flask,Response,request
from flask_restful import Resource
from flask_mysqldb import MySQL
from flask import Response
import json
app = Flask(__name__)

mysql = MySQL(app)

class AddExamFitb(Resource):
    def post(self):
        json_raw = request.get_json()
        index = 0;
        for i in json_raw:
            try:
                
                for answer in i['anwser_all']:
                    print(answer)
                  
                    #cur = mysql.connection.cursor()
                    #cur.execute(sql)
                    #mysql.connection.commit()

            except:
                
                anwser = ''
                count = 0
                for anws in i['anwser']:
                    if(len(i['anwser']) != count+1):
                        anwser += anws+"," 
                        count+=1    
                    else:
                        anwser +=anws
                print(anwser)

                sql = "SELECT user_id from user_login where username = '"+i["teacher"]+"';"
                cur = mysql.connection.cursor()
                cur.execute(sql)
                u_id = cur.fetchall()
                cur.close()
                print(i['question'])

                sql = "SELECT question_id from template_question_fitb;"
                cur = mysql.connection.cursor()
                cur.execute(sql)
                q_id = cur.fetchall()
                cur.close()
                print(i['question'])
               
                sql = "insert into temp_question_fitb (question , anwser ,user_id,question_id)values("+"'"+i['question']+"','"+anwser+"','"+str(u_id[0][0])+"','"+q_id[index][0]+"');"
                cur = mysql.connection.cursor()
                cur.execute(sql)
                mysql.connection.commit()
                index+=1