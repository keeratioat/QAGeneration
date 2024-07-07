from flask import render_template,request,redirect,session,url_for,make_response
import hashlib
import requests
from flask import Blueprint
from controller.allowed_file import allowed_file_add_user
import os
import csv
import pdfkit

manage_route = Blueprint('manage_user_route' , __name__ ,template_folder='templates')

@manage_route.route('/manage_user' , methods=["GET", "POST"])
def manage_user():
    if (session.get("status") != 'teacher' and session.get("status") != 'admin'):
          return redirect(url_for('login_route.not_permission'))
    
    if(request.method == 'POST'):
        search = request.form['search']
        search_json = {
            'search' : search,
            
        }
        response = requests.post('http://127.0.0.1:5000/search_user',json=search_json)
        response_result = response.json();
        print(response_result)
        return render_template("manage_user.html",user = response_result)


    std_json = {
        'first_name' : session['firstname'],
        'lastname' : session['lastname'],
        'subject' : session['subject_name'],
        'section' :session['section']
    }

    response = requests.get('http://127.0.0.1:5000/std_info' ,json=std_json)
    response_result = response.json();
    print(response_result)
    return render_template("manage_user.html",user = response_result)

@manage_route.route('/manage_user/<user_id>' , methods=["GET", "POST"])
def manage_user_delete(user_id):
    if (session.get("status") != 'teacher' and session.get("status") != 'admin'):
          return redirect(url_for('login_route.not_permission'))
    response = requests.delete('http://127.0.0.1:5000/user_detail/'+user_id)
    response_result = response.json();
    print(response_result)
    
    return redirect(url_for('manage_user_route.manage_user'))

@manage_route.route('/manage_exam' , methods=["GET", "POST"])
def manage_exam():
    if (session.get("status") != 'teacher' and session.get("status") != 'admin'):
          return redirect(url_for('login_route.not_permission'))
    teacher_name_json = {
        'teacher' :  session['user_id']
    }
    response = requests.get('http://127.0.0.1:5000/show_all_exam' ,json=teacher_name_json)
    all_exam = response.json();
    print(all_exam)

    return render_template("manage_exam.html" ,all_exam = all_exam)

@manage_route.route('/manage_subject' , methods=["GET", "POST"])
def manage_subject():
    if (session.get("status") != 'teacher' and session.get("status") != 'admin'):
          return redirect(url_for('login_route.not_permission'))
    response = requests.get('http://127.0.0.1:5000/subject')
    response_result = response.json();
    print(response_result)

    return render_template("manage_subject.html" ,subject = response_result )

@manage_route.route('/manage_subject/<subject_id>' , methods=["GET", "POST"])
def manage_subject_delete(subject_id):
    if (session.get("status") != 'teacher' and session.get("status") != 'admin'):
          return redirect(url_for('login_route.ot_permission'))
    response = requests.delete('http://127.0.0.1:5000/subject/'+subject_id)
    response_result = response.json();
    print(response_result)

    response = requests.get('http://127.0.0.1:5000/subject')
    response_result = response.json();
    print(response_result)
    return redirect(url_for('manage_user_route.manage_subject'))

@manage_route.route('/delete_select_user' , methods=["GET", "POST"])
def delete_select_user():
    select_user = request.form.getlist("delete_select_user")
    
    for user in select_user:
        response = requests.delete('http://127.0.0.1:5000/user_detail/'+user)
        response_result = response.json();
    
    return redirect(url_for('manage_user_route.manage_user')) 

@manage_route.route('/add_user' , methods=["GET", "POST"])
def add_user():
    if (session.get("status") != 'teacher' and session.get("status") != 'admin'):
          return redirect(url_for('login_route.not_permission'))
    if (request.method == 'POST'):
        if len(session['section']) > 2:
            name = request.form['name']
            lastname = request.form['lastname']
            pwd = request.form['stdId']
            username = request.form['stdId']
            sec = request.form['section']

            pwdHash = hashlib.md5(pwd.encode())

            add_user_json = {
                    'name' : name,
                    'lastname' : lastname,
                    'pwd' : pwdHash.hexdigest(),
                    'username' : username,
                    'status' : 'student',
                    'sub_name' : 'OBJECT-ORIENTED SOFTWARE DEVELOPMENT',
                    'section' : sec,
                }
            response = requests.post('http://127.0.0.1:5000/add_user', json=add_user_json)
            response_result = response.json();
            print(response_result)
        
            return redirect(url_for('manage_user_route.manage_user'))


        else:
            name = request.form['name']
            lastname = request.form['lastname']
            pwd = request.form['stdId']
            username = request.form['stdId']
        

            print(len(username))

            pwdHash = hashlib.md5(pwd.encode())

            add_user_json = {
                    'name' : name,
                    'lastname' : lastname,
                    'pwd' : pwdHash.hexdigest(),
                    'username' : username,
                    'status' : 'student',
                    'sub_name' : 'OBJECT-ORIENTED SOFTWARE DEVELOPMENT',
                    'section' : str(session['section']),
                }
            response = requests.post('http://127.0.0.1:5000/add_user', json=add_user_json)
            response_result = response.json();
            print(response_result)
        
            return redirect(url_for('manage_user_route.manage_user'))
    list_of_sec = []
    if(len(session['section']) > 2):
         list_of_sec =  str(session['section']).split(",")
    return render_template("add_user.html" ,list_of_sec = list_of_sec)

@manage_route.route('/add_user_csv' , methods=["GET", "POST"])
def add_user_csv():
    if request.method == 'POST':
        file = request.files['file']
        
        if file and allowed_file_add_user(file.filename):
            if not os.path.isdir(session['uname']):
                os.mkdir(session['uname'])
            
            file.save(os.path.join(session['uname'],file.filename))

            user_data = []
            with open(session['uname']+'/'+file.filename, encoding="utf8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    user_data.append(row)
            print(user_data)

            if len(session['section']) > 2:
                sec = request.form['section']
                for user in user_data:
                    pwdHash = hashlib.md5(user['username'].encode())
                    add_user_json = {
                    'name' : user['name'],
                    'lastname' : user['lastname'],
                    'pwd' : pwdHash.hexdigest(),
                    'username' : user['username'],
                    'status' : 'student',
                    'sub_name' : 'OBJECT-ORIENTED SOFTWARE DEVELOPMENT',
                    'section' : sec,
                }
                    response = requests.post('http://127.0.0.1:5000/add_user', json=add_user_json)
                    response_result = response.json();

                return redirect(url_for('manage_user_route.manage_user')) 
            else:
                for user in user_data:
                    pwdHash = hashlib.md5(user['username'].encode())
                    add_user_json = {
                    'name' : user['name'],
                    'lastname' : user['lastname'],
                    'pwd' : pwdHash.hexdigest(),
                    'username' : user['username'],
                    'status' : 'student',
                    'sub_name' : 'OBJECT-ORIENTED SOFTWARE DEVELOPMENT',
                    'section' : str(session['section']),
                }
                    response = requests.post('http://127.0.0.1:5000/add_user', json=add_user_json)
                    response_result = response.json();

                return redirect(url_for('manage_user_route.manage_user'))    
        else:
            print("input file .csv")
    list_of_sec = []
    if(len(session['section']) > 2):
         list_of_sec =  str(session['section']).split(",")
    return render_template("add_user_csv.html" , list_of_sec = list_of_sec)

@manage_route.route('/add_subject' , methods=["GET", "POST"])
def add_subject():
    if (session.get("status") != 'teacher' and session.get("status") != 'admin'):
          return redirect(url_for('login_route.not_permission'))
    if (request.method == 'POST'):
        sub_id = request.form['sub_id']
        sub_name = request.form['sub_name']
        print(sub_id + " "+ sub_name)
        sub_json = {
            'sub_id' : sub_id,
            'sub_name' : sub_name
        }
        response = requests.post('http://127.0.0.1:5000/add_subject', json=sub_json)
        response_result = response.json();
        print(response_result)
        return redirect(url_for('manage_user_route.manage_subject'))
    return render_template("add_subject.html")

@manage_route.route('/edit_subject/<sub_id>/<sub_name>' , methods=["GET", "POST"])
def edit_subject(sub_id,sub_name):
    if (session.get("status") != 'teacher' and session.get("status") != 'admin'):
          return redirect(url_for('login_route.not_permission'))
    session['sub_id'] = sub_id
    return render_template("edit_subject.html",sub_id = sub_id, sub_name = sub_name)

@manage_route.route('/edit_subject' , methods=["GET", "POST"])
def edit_subject2():
    if (session.get("status") != 'teacher' and session.get("status") != 'admin'):
          return redirect(url_for('login_route.not_permission'))
    if (request.method == 'POST'):
        old_sub_id = session['sub_id']
        sub_id = request.form['sub_id']
        sub_name = request.form['sub_name']
        print(sub_id + " "+ sub_name)
        sub_json = {
            'old_sub_id' : old_sub_id,
            'sub_id' : sub_id,
            'sub_name' : sub_name
        }
        response = requests.put('http://127.0.0.1:5000/edit_subject', json=sub_json)
        response_result = response.json();
        print(response_result)
        return redirect(url_for('manage_user_route.manage_user'))
    return render_template("edit_subject.html")

@manage_route.route('/edit_user/<firstname>/<lastname>/<section>/' , methods=["GET", "POST"])
def edit_user(firstname,lastname,section):
    if (session.get("status") != 'teacher' and session.get("status") != 'admin'):
          return redirect(url_for('login_route.not_permission'))

    session['old_firstname'] = firstname
    session['old_lastname'] = lastname
    return render_template("edit_user.html", firstname=firstname,lastname=lastname,section=section)

@manage_route.route('/edit_user' , methods=["GET", "POST"])
def edit_user2():
    if (session.get("status") != 'teacher' and session.get("status") != 'admin'):
          return redirect(url_for('login_route.not_permission'))
    if (request.method == 'POST'):
        name = request.form['name']
        lastname = request.form['lastname']
        status = "student"
        sub_name = "OBJECT-ORIENTED SOFTWARE DEVELOPMENT"
        section = request.form['section']
        

        print(name , " " ,lastname , " " , status , " " ,sub_name, " ",section)

        user_json = {
            'name' : name,
            'lastname' : lastname,
            'status' : status,
            'sub_name' :sub_name,
            'section' :section,
            'old_name' : session['old_firstname'],
            'old_lastname' :session['old_lastname']
        }
        response = requests.put('http://127.0.0.1:5000/edit_user', json=user_json)
        response_result = response.json();    
        print(response_result)
        return redirect(url_for('manage_user_route.manage_user'))
    return render_template("edit_user.html")

@manage_route.route('/delete_exam/<exam_name>' , methods=["GET", "POST"])
def delete_exam(exam_name):
    print(exam_name)
    response = requests.delete('http://127.0.0.1:5000/delete_exam/'+exam_name)
    response_result = response.json();
    print(response_result)

    return redirect(url_for('manage_user_route.manage_exam'))
    
@manage_route.route('/delete_temp_exam' , methods=["GET", "POST"])
def delete_temp_exam():
    response = requests.delete('http://127.0.0.1:5000/delete_temp_exam')
    response_result = response.json();
    return redirect(url_for('teacher_route.upload_file'))

@manage_route.route('/std_pdf' , methods=["GET", "POST"])
def std_pdf():
    std_json = {
        'first_name' : session['firstname'],
        'lastname' : session['lastname'],
        'subject' : session['subject_name'],
        'section' :session['section']
    }

    response = requests.get('http://127.0.0.1:5000/std_info' ,json=std_json)
    std = response.json();
    print(std)

    res = render_template("std_pdf.html" , std =std)
    res_string = pdfkit.from_string(res)
    response = make_response(res_string ,False)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline;filename=exam.pdf'

    return response

@manage_route.route('/select_add_user' , methods=["GET", "POST"])
def select_add_user():

    return render_template("select_add_user.html")