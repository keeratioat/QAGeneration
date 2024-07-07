
from time import sleep
from flask import render_template,request,redirect,session,url_for,make_response
import os
import requests
from controller.generate_qa import *
from controller.complie import compile_java
from controller.allowed_file import allowed_file_exam
from flask import Blueprint
import pdfkit
import json

teacher_route = Blueprint('teacher_route' , __name__ ,template_folder='templates')

@teacher_route.route('/upload_file' , methods=["GET", "POST"])
def upload_file():
    if (session.get("status") != 'teacher' and session.get("status") != 'admin'):
          return redirect(url_for('login_route.not_permission'))
    if request.method == "POST":
        files = request.files.getlist("file[]")

        if not os.path.isdir(session['uname']):
            os.mkdir(session['uname'])
        className = [file.filename.replace('.java','') for file in files]
        for file in files:
            if file and allowed_file_exam(file.filename):
                file.save(os.path.join(session['uname'],file.filename))
                compile_java(session['uname']+'/'+file.filename)
                sleep(2)
                print(session['uname']+file.filename)
                file_path_json = {
                    'file_path' : session['uname']+'/'+file.filename,
                    'teacher' : session['uname']
                    }
                response = requests.post('http://127.0.0.1:5000/files',json=file_path_json)
                response_result = response.json();
                print(response_result)          
            else:
                print("plese upload .java or .class file") 
                return redirect(request.url)        
        
        mcq_api_response = requests.get('http://127.0.0.1:5000/template_question_mcq')
        mcq_api_response_result = mcq_api_response.json();

        fitb_api_response = requests.get('http://127.0.0.1:5000/template_question_fitb')
        fitb_api_response_result = fitb_api_response.json();

        q_api_response = requests.get('http://127.0.0.1:5000/template_question')
        q_api_response_result = q_api_response.json();

        mcq = generate_mcq(className ,mcq_api_response_result)
        q_f_in_the_bank = generate_fill_in_the_bank(className ,fitb_api_response_result)
        question = generate_question(q_api_response_result)
        
        print(q_f_in_the_bank)
        print(question)

        print(mcq)
        response = requests.post('http://127.0.0.1:5000/add_exam_mcq',json=mcq)
        response_result = response.json();

        response = requests.post('http://127.0.0.1:5000/add_exam_fibt',json=q_f_in_the_bank)
        response_result = response.json();
        
        response = requests.post('http://127.0.0.1:5000/add_exam_question',json=question)
        response_result = response.json();

        return redirect(url_for('teacher_route.add_exam'))       

    return render_template("uploadfile.html")
    
@teacher_route.route('/add_exam_detail' , methods=["GET", "POST"])
def addexamdetail():
    if (session.get("status") != 'teacher' and session.get("status") != 'admin'):
          return redirect(url_for('login_route.not_permission'))  
          
    return render_template("add_exam_detail.html")

@teacher_route.route('/show_temp_detail' , methods=["GET", "POST"])
def show_temp_detail():
    if request.method == 'POST':
        questions = request.form.getlist("question")
        point = request.form.getlist("point")
        question = []
        point_2 = []
        points =[]
        for p in point:
            if len(p) > 0:
                point_2.append(p) 
        print(questions)
        print(point)
        print(point_2)

        question_p = []

        response = requests.get('http://127.0.0.1:5000/temp_question')
        temp_q = response.json();

        for ques in questions: 
            for qq in temp_q: 
                if(ques == qq['question']):
                    question_p.append(ques)
        print(question_p)
        
        for q in questions:      
            question_json = {
                'question' :q,
                'teacher' :session['uname']
            }
            question.append(question_json)
        print(question)

        print("question_p :"+str(question_p))
        print("point_2 :"+str(point_2))
        for i in range(len(point_2)):
            point_json = {
                'question' : question_p[i],
                'point' : point_2[i],
                
            }
            points.append(point_json)

        response = requests.post('http://127.0.0.1:5000/select_question',json=question)
        response_result = response.json();

        response = requests.put('http://127.0.0.1:5000/select_question',json=points)

        
        print(response_result)
    teacher_json = {
                'teacher' : session['uname'],
                
            }
    response = requests.get('http://127.0.0.1:5000/show_temp_detail',json=teacher_json)
    exam_detail = response.json();
    return render_template("show_temp_detail.html" ,exam_detail =exam_detail)

@teacher_route.route('/std_info' , methods=["GET", "POST"])
def std_info():
    std_json = {
        'first_name' : session['firstname'],
        'lastname' : session['lastname'],
        'subject' : session['subject_name'],
        'section' :session['section']
    }
    
    response = requests.get('http://127.0.0.1:5000/std_info' ,json=std_json)
    result = response.json();
    print(result)
    return render_template("student_info.html" ,std=result)

@teacher_route.route('/all_exam' , methods=["GET", "POST"])
def all_exam():
    if (session.get("status") != 'teacher' and session.get("status") != 'admin'):
          return redirect(url_for('login_route.not_permission'))
    teacher_name_json = {
        'teacher' :  session['user_id']
    }
    response = requests.get('http://127.0.0.1:5000/show_all_exam' ,json=teacher_name_json)
    all_exam = response.json();
    print(all_exam)
    return render_template("all_exam_info.html" , all_exam = all_exam)

@teacher_route.route('/change_status_exam_open/<exam_name>/<exam_status>' , methods=["GET", "POST"])
def change_status_exam_open(exam_name,exam_status):
    print(exam_name)
    print(exam_status)
    json_exam_info  = {
        'exam_name': exam_name,
        'exam_status' : exam_status,
        'teacher' : session['user_id']
    }
    print(json_exam_info)
    response = requests.put('http://127.0.0.1:5000/change_exam_status_open' ,json=json_exam_info)
    result = response.json();


    return redirect(url_for('teacher_route.all_exam'))

@teacher_route.route('/change_status_exam_close/<exam_name>/<exam_status>' , methods=["GET", "POST"])
def change_status_exam_close(exam_name,exam_status):
    print(exam_name)
    print(exam_status)
    json_exam_info  = {
        'exam_name': exam_name,
        'exam_status' : exam_status,
        'teacher' : session['user_id']
    }
    print(json_exam_info)
    response = requests.put('http://127.0.0.1:5000/change_exam_status_close' ,json=json_exam_info)
    result = response.json();


    return redirect(url_for('teacher_route.all_exam'))

@teacher_route.route('/check_question' , methods=["GET", "POST"])
def check_question():
    section_json = {
        'uname' : session['user_id'],
        'sec' : session['section']
    }
    response = requests.get('http://127.0.0.1:5000/exam_point_name' ,json = section_json)
    exam_name = response.json();
    print(exam_name)
    return render_template("std_check_question.html" ,std = exam_name)

@teacher_route.route('/check_question/<exam_name>' , methods=["GET", "POST"])
def check_question_exam(exam_name):
    json_point_exam = {
        'teacher' : session['user_id'],
        'exam_name' : exam_name
    }
    response = requests.get('http://127.0.0.1:5000/student_anwser' ,json=json_point_exam)
    result = response.json();
    print(result)
    
    return render_template("check_question.html" , std = result)

@teacher_route.route('/exam_check/<std_uname>/<exam_name>/<firstname>/<lastname>' , methods=["GET", "POST"])
def exam_check(std_uname,exam_name,firstname,lastname):
    print(std_uname , " " , exam_name)
    std_json = {
        'std_uname' : std_uname,
        'exam_name' : exam_name
    }
    response = requests.get('http://127.0.0.1:5000/show_anwser_std' ,json=std_json)
    result = response.json();
    print(result)
    return render_template("exam_check.html" ,anwser = result ,firstname=firstname,lastname=lastname,exam_name=exam_name,student=std_uname)

@teacher_route.route('/std_point' , methods=["GET", "POST"])
def std_point_exam_name():
    section_json = {
        'uname' : session['user_id'],
        'sec' : session['section']
    }
    print(section_json)
    response = requests.get('http://127.0.0.1:5000/exam_point_name' ,json = section_json)
    exam_name = response.json();
    print(exam_name)

    return render_template('std_point_exam_name.html' ,std = exam_name)

@teacher_route.route('/std_point/<exam_name>' , methods=["GET", "POST"])
def std_point(exam_name):
    print(exam_name)
    exam_json = {
        'uname' : session['uname'],
        'sec' : session['section'],
        'exam_name' : exam_name
    }
    response = requests.get('http://127.0.0.1:5000/std_point' ,json = exam_json)
    std_point = response.json();
    print(std_point)
    return render_template('std_point.html' ,exam_name = exam_name ,std_point=std_point)

@teacher_route.route('/std_point_pdf/<exam_name>' , methods=["GET", "POST"])
def std_point_pdf(exam_name):
    exam_json = {
        'uname' : session['uname'],
        'sec' : session['section'],
        'exam_name' : exam_name
    }

    response = requests.get('http://127.0.0.1:5000/std_point' ,json = exam_json)
    std_point = response.json();

    res = render_template("std_point_pdf.html" ,exam_name = exam_name, std_point =std_point)
    res_string = pdfkit.from_string(res)
    response = make_response(res_string ,False)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline;filename=exam.pdf'
    
    return response

@teacher_route.route('/create_comp' , methods=["GET", "POST"])
def create_comp():
    if request.method == "POST":
        exam_name = request.form['exam_name']
        exam_detail = request.form['exam_detail']
        hr = request.form['hr']
        min = request.form['min']
        sec = request.form['sec']
        teacher = session['uname']
        section = session['section']
        subject_name = session['subject_name']

        exam_detail_json = {
            'exam_name' : exam_name,
            'exam_detail' : exam_detail,
            'hr' : hr,
            'min' : min,
            'sec' : sec,
            'teacher' : session['user_id'],
            'section' : section,
            'subject_name': subject_name

        }
        response = requests.post('http://127.0.0.1:5000/add_exam_detail',json=exam_detail_json)
        response_result = response.json();
        print(response_result)

        response = requests.delete('http://127.0.0.1:5000/select_question')
    return render_template("create_exam_complate.html")

@teacher_route.route('/add_exam' , methods=["GET", "POST"])
def add_exam():
    response = requests.get('http://127.0.0.1:5000/temp_question_fitb')
    fitb_questions = response.json();
    response = requests.get('http://127.0.0.1:5000/temp_question_mcq')
    mcq_question = response.json();
    response = requests.get('http://127.0.0.1:5000/temp_question')
    questions = response.json();
    
    return render_template("add_exam.html" ,fitb_ques = fitb_questions ,mcq_question =mcq_question ,questions = questions)

@teacher_route.route('/exam_pdf/<exam_name>' , methods=["GET", "POST"])
def exam_pdf(exam_name):
    exam_name_json = {
        'exam_name' : exam_name
    }
    response = requests.get('http://127.0.0.1:5000/all_exam', json=exam_name_json)
    exams = response.json();
    print(exams)

    res = render_template("exam_pdf.html" , exams =exams)
    res_string = pdfkit.from_string(res)
    response = make_response(res_string ,False)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline;filename=exam.pdf'

    return response

@teacher_route.route('/std_point_exam' , methods=["GET", "POST"])
def std_point_exam():
    if request.method == "POST":
        output = request.get_json()
        print(output) # This is the output that was stored in the JSON within the browser
        print(type(output))
        result = json.loads(output) #this converts the json output to a python dictionary
        print(result) # Printing the new dictionary
        print(type(result))#this shows the json converted as a python dictionary


        total_point_quetion = 0
        student = ""
        exam_name = ""
        for i in result:
            total_point_quetion += i['point']   
            student = i['student']
            exam_name = i['exam_name']

        print(total_point_quetion)

        json_point_exam = {
            'total_point_quetion' : total_point_quetion,
            'student' : student,
            'exam_name' : exam_name
        }
        response = requests.put('http://127.0.0.1:5000/edit_total_point_question', json=json_point_exam)

        response = requests.put('http://127.0.0.1:5000/edit_point_question', json=result)

        return {'Massage':'check_anwser_complte'}

       

    if request.method == "GET":
        return render_template('check_exam_comp.html')
    
@teacher_route.route('/main_page' , methods=["GET", "POST"])
def main_page():
    return render_template('main_page.html')