from flask import render_template,request,redirect,session,url_for
import requests
from controller.generate_qa import *
import json
from flask import Blueprint
import hashlib

std_route = Blueprint('std_route' , __name__ ,template_folder='templates')
@std_route.route('/examchoice/<exam_name>' , methods=["GET", "POST"])
def examchoice(exam_name):
    if not session.get("status"):
          return redirect(url_for('login_route.not_permission'))
    std_name = session['uname']
    json = {
        'std_name': std_name
    }

    exam_name_json = {
        'exam_name' : exam_name
    }


    response = requests.get('http://127.0.0.1:5000/files', json=exam_name_json)
    file_path = response.json();
    print(file_path)

    code_text = ""
    for java_file in file_path:
        f = open(java_file['java_file_path'], "r")
        code_text += f.read()

    print(code_text)

    
    response = requests.get('http://127.0.0.1:5000/all_exam', json=exam_name_json)
    exam = response.json();

    return render_template("examchoice.html" , code_text = code_text ,exam= exam ,hr=session['hr'] ,min=session['min'],sec=session['sec'])

@std_route.route('/history_examination' , methods=["GET", "POST"])
def history_examination():
    json = {
            'user_name' : session['user_id']
            
        }
    response = requests.get('http://127.0.0.1:5000/history_exam', json=json)
    all_history_exam = response.json();
    print(all_history_exam)
    
    return render_template("history_examination.html" ,all_history=all_history_exam)

@std_route.route('/examdetail/<exam_name>' , methods=["GET", "POST"])
def examdetail(exam_name):
    if not session.get("status"):
          return redirect(url_for('login_route.not_permission'))
    json = {
            'exam_name' : exam_name
            
        }
    response = requests.get('http://127.0.0.1:5000/exam_detail', json=json)
    exam_detail = response.json();
    print(exam_detail)
    session['hr'] = exam_detail['hour']
    session['min'] = exam_detail['min']
    session['sec'] = exam_detail['sec']
    session['exam_name'] = exam_detail['exam_name']

    return render_template("examdetail.html" , exam_detail = exam_detail)

@std_route.route('/std_anwser' , methods=["GET", "POST"])
def std_anwser():
    if request.method == "POST":
        session.pop('hr',None)
        session.pop('min',None)
        session.pop('sec',None)
    
        output = request.get_json()
        print(output) # This is the output that was stored in the JSON within the browser
        print(type(output))
        result = json.loads(output) #this converts the json output to a python dictionary
        print(result) # Printing the new dictionary
        print(type(result))#this shows the json converted as a python dictionary

        student_anwser = []
        mcq_point = 0
        fitb_point = 0
        for i in result:
 
            if(i['exam_type'] == 'mcq'):
                if('anwser' in i):
                    if(i['correct_choice'] == i['anwser']):
                        mcq_point+=1

            if(i['exam_type'] == 'fitb'):
                if('anwser' in i):
                    if(i['all_anwser'] == i['anwser']):
                        fitb_point+=1
            if(i['exam_type'] == 'question'):
                if('anwser' in i):
                    student_anwser.append({
                        'question' : i['question'],
                        'anwser' :  i['anwser']
                    })
        print(session['exam_name'])
        print("mcq_point: ",mcq_point)
        print("fitb_point: ",fitb_point)
    
        print(student_anwser)
        print(session['exam_name'])

    
        for i in student_anwser:
            std_anwser_json = {
                'question' : i['question'],
                'anwser' : i['anwser'],
                'exam_name' : session['exam_name'],
                'student' : str(session['user_id'])
            }
            response = requests.post('http://127.0.0.1:5000/student_anwser', json=std_anwser_json)
            result = response.json()
    
        exam_point_json ={
            'mcq' : mcq_point,
            'fitb' : fitb_point,
            'exam_name' : session['exam_name'],
            'student' : session['user_id']
          
        }

        

        print(exam_point_json)
        response = requests.post('http://127.0.0.1:5000/exam_point', json=exam_point_json)
        result = response.json()

        std_exam_status = {
            'exam_name' : session['exam_name'],
            'student' : str(session['user_id'])
        }
        response = requests.put('http://127.0.0.1:5000/student_anwser', json=std_exam_status)
        result = response.json()

        return {'massage' : 'send complete'}

    if request.method == "GET":
        return render_template("exam_comp.html")
        
@std_route.route('/select_exam' , methods=["GET", "POST"])
def select_exam():
    json = {
            'user_name' : session['user_id']
            
        }
    response = requests.get('http://127.0.0.1:5000/select_exam', json=json)
    select_exam = response.json();
    print(select_exam)
    return render_template("select_exam.html" ,exam=select_exam)

@std_route.route('/exam_comp' , methods=["GET", "POST"])
def exam_comp():
    return render_template("exam_comp.html")
    
@std_route.route('/main_page_std' , methods=["GET", "POST"])
def main_page_std():
    return render_template("main_page_std.html")

@std_route.route('/change_pwd' , methods=["GET", "POST"])
def change_pwd():
    if request.method == "POST":
        pwd = request.form['pwd']
        con_pwd = request.form['con_pwd']

        if(pwd == con_pwd): 
            pwdHash = hashlib.md5(pwd.encode())
            print(pwdHash.hexdigest())
            print(session['uname'])

            json_change_pwd = {
                'pwd_new' : pwdHash.hexdigest(),
                'uname' : session['uname']
            }
            print(json_change_pwd)
            response = requests.put('http://127.0.0.1:5000/change_pwd', json=json_change_pwd)
           
            result = response.json()
            print(result)

            return render_template("change_pwd_comp.html")

    return render_template("change_pwd.html")