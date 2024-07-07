from flask import Flask
from flask_mysqldb import MySQL
from flask_restful import Api
from resource.index import Index
from resource.login import Login
from resource.user_detail import UserDetail
from resource.subject import Subject
from resource.delete_subject import DeleteSubject
from resource.add_subject import AddSubject
from resource.delete_user import DeleteUser
from resource.add_user import AddUser
from resource.search_user import SearchUser
from resource.edit_subject import EditSubject
from resource.edit_user import EditUser
from resource.files import Files
from resource.add_exam_mcq import AddExamMcq
from resource.add_exam_fill import AddExamFitb
from resource.add_exam_question import AddQuestionExam
from resource.temp_question_exam_fitb import TempQuestionExamFitb
from resource.temp_anwser_exam_fitb import TempAnwserExamFitb
from resource.temp_mcq import TempQuestionExamMcq
from resource.temp_question import TempQuestionExam
from resource.select_question import SelectQuestion
from resource.add_exam_detail import AddExamDetail
from resource.exam_detail import ExamDetail
from resource.exam_info import ExamInfo
from resource.show_all_exam import ShowAllExam
from resource.change_exam_status_close import ChangeExamStatusClose
from resource.change_exam_status_open import ChangeExamStatusOpen
from resource.get_teacher_name import GetTeacherNameStd
from resource.all_exam import AllExam
from resource.select_exam import SelectExam 
from resource.delete_exam import DeleteExam
from resource.exam_point import ExamPoint
from resource.history_examination import HistoryExamination
from resource.studeunt_anwser import StudentAnwser
from resource.std_point import StdPoint
from resource.std_info import StdInfo
from resource.show_anwser_std import ShowAnwserStd
from resource.delete_temp_exam import DeleteTempExam
from resource.edit_total_point_question import EditTotalPointQuestion
from resource.exam_point_name import ExamPointName
from resource.change_pwd import ChangePwd
from resource.edit_point_question import EditPointQuestion
from resource.show_temp_detail import ShowTempDetail
from resource.template_question import TemplateQuestion
from resource.template_question_fitb import TemplateQuestionFitb
from resource.template_question_mcq import TemplateQuestionMcq
from config import Config

app = Flask(__name__)
mysql = MySQL(app)
api = Api(app)
app.config.from_object(Config)

api.add_resource(Index , '/')
api.add_resource(Login , '/login')
api.add_resource(UserDetail , '/user_detail')
api.add_resource(Subject , '/subject')
api.add_resource(DeleteSubject , '/subject/<id>')
api.add_resource(AddSubject , '/add_subject')
api.add_resource(DeleteUser , '/user_detail/<id>')
api.add_resource(AddUser ,'/add_user')
api.add_resource(SearchUser ,'/search_user')
api.add_resource(EditSubject , '/edit_subject')
api.add_resource(EditUser , '/edit_user')
api.add_resource(Files ,'/files')
api.add_resource(AddExamMcq , '/add_exam_mcq')
api.add_resource(AddExamFitb , '/add_exam_fibt')
api.add_resource(AddQuestionExam , '/add_exam_question')
api.add_resource(TempQuestionExamFitb, '/temp_question_fitb')
api.add_resource(TempAnwserExamFitb, '/temp_awnser_fitb')
api.add_resource(TempQuestionExamMcq, '/temp_question_mcq')
api.add_resource(TempQuestionExam , '/temp_question')
api.add_resource(SelectQuestion, '/select_question')
api.add_resource(AddExamDetail , '/add_exam_detail')
api.add_resource(ExamDetail , '/exam_detail')
api.add_resource(ExamInfo,'/exam_info')
api.add_resource(ShowAllExam, '/show_all_exam')
api.add_resource(ChangeExamStatusClose , '/change_exam_status_close')
api.add_resource(ChangeExamStatusOpen , '/change_exam_status_open')
api.add_resource(GetTeacherNameStd , '/get_teacher_name')
api.add_resource(AllExam , '/all_exam')
api.add_resource(SelectExam,'/select_exam')
api.add_resource(DeleteExam,'/delete_exam/<exam_name>')
api.add_resource(DeleteTempExam,'/delete_temp_exam')
api.add_resource(ExamPoint,'/exam_point')
api.add_resource(HistoryExamination,'/history_exam')
api.add_resource(StudentAnwser,'/student_anwser')
api.add_resource(StdPoint,'/std_point')
api.add_resource(StdInfo,'/std_info')
api.add_resource(ShowAnwserStd,'/show_anwser_std')
api.add_resource(EditTotalPointQuestion, '/edit_total_point_question')
api.add_resource(ExamPointName,'/exam_point_name')
api.add_resource(ChangePwd , '/change_pwd')
api.add_resource(EditPointQuestion ,'/edit_point_question')
api.add_resource(ShowTempDetail ,'/show_temp_detail')
api.add_resource(TemplateQuestion , '/template_question')
api.add_resource(TemplateQuestionMcq , '/template_question_mcq')
api.add_resource(TemplateQuestionFitb , '/template_question_fitb')

if __name__ == "__main__":
     app.run(debug=True)