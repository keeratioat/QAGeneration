
from flask import render_template,request,redirect,session,url_for

import hashlib
import requests

from flask import Blueprint

login_route = Blueprint('login_route' , __name__ ,template_folder='templates')

@login_route.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@login_route.route('/login' , methods=["GET", "POST"])
def login():
    
    if (request.method == 'POST'):
        uname = request.form['uname']
        pwd = request.form['pwd']
        print(uname)
        print(len(pwd))

        if(len(pwd) == 0):
            login_json = {
            'user_name' : uname,
            'password' : pwd
            }
        else:
            pwdHash = hashlib.md5(pwd.encode())
            login_json = {
                'user_name' : uname,
                'password' : pwdHash.hexdigest()
            }
        response = requests.post('http://127.0.0.1:5000/login', json=login_json)
        response_result = response.json();
        if(len(response_result) == 1):
            session['uname'] = response_result[0]['username'] 
            session['firstname'] = response_result[0]['firstname']
            session['lastname'] = response_result[0]['lastname']
            session['status'] = response_result[0]['status']
            session['section'] = response_result[0]['section']
            session['subject_name'] = response_result[0]['subject_name']
            session['user_id'] = response_result[0]['user_id']

            if(response_result[0]['status'] == 'student'):
                
                return redirect(url_for('std_route.main_page_std'))

            if(response_result[0]['status'] == 'teacher'):
                
                return redirect(url_for('teacher_route.main_page'))
            if(response_result[0]['status'] == 'admin'):
                
                return redirect(url_for('teacher_route.main_page'))

        else:
            print("Not have user")      

    return render_template("login.html")

@login_route.route('/login_std' , methods=["GET", "POST"])
def login_std():
    return render_template("login_std.html")

@login_route.route('/login_teacher' , methods=["GET", "POST"])
def login_teacher():
    return render_template("login_teacher.html")

@login_route.route('/logout' , methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect(url_for('login_route.index'))

#Permision Page
@login_route.route('/not_permission' , methods=["GET", "POST"])
def not_permission():
    return render_template("not_permission.html")