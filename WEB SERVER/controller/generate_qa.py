from jpype import startJVM,JClass
from random import randint ,shuffle
from flask import session
from controller.choice import *
import collections
startJVM(convertStrings=False)
def generate_mcq(className , mcq_question):
    print(mcq_question)
    random_class_name = className[randint(0,len(className)-1)]

    javaclass = JClass(session['uname']+"."+random_class_name)()
    cons = javaclass.getClass().getDeclaredConstructors()
    classname = javaclass.getClass().getSimpleName()
    attname = javaclass.getClass().getDeclaredFields()
    methods = javaclass.getClass().getDeclaredMethods()
    
    questions =[]
    question={}
    #print(person.getClass().getSuperclass().getSimpleName())
    
    question1 = mcq_question[0]['question'].replace('<classname>',str(classname))
    question2 = mcq_question[1]['question'].replace('<classname>',str(classname))
    question3 = mcq_question[2]['question'].replace('<classname>',str(classname))
    question4 = mcq_question[3]['question'].replace('<classname>',str(classname))
    question5 = mcq_question[4]['question'].replace('<classname>',str(classname))
    question6 = mcq_question[5]['question'].replace('<classname>',str(classname))
    question7 = mcq_question[6]['question'].replace('<classname>',str(classname))
    question8 = mcq_question[7]['question'].replace('<classname>',str(classname))
    question9 = mcq_question[8]['question'].replace('<classname>',str(classname))
    question10 = mcq_question[9]['question'].replace('<classname>',str(classname))

    print(''+question1)
    
    ChoiceQ1 = choiceNumber(len(className))
    
    print(ChoiceQ1)
    shuffle(ChoiceQ1)
    print(ChoiceQ1)
    question['question'] = question1
    question['Choice'] = ChoiceQ1
    question['Correct_Ans'] = len(className)
    question['teacher'] = session['uname']
    print(question)
    questions.append(question)
    print(questions)

    question = {}
    
    print(''+ question2)
    class_name_q2 =[]
    for cn in className:
        class_name_q2.append(cn)
    
    s = ""
    count = 0
    for i in class_name_q2:

        if(len(class_name_q2) != count+1):
            s += i+" "
            count += 1
        else:
            s += i
    choice2 = choiceMultiClassName(className,s)
    shuffle(choice2)
    print('-----------')
    print(choice2)
    print('-----------')
    question['question'] = question2
    question['Choice'] = choice2
    question['Correct_Ans'] = s
    question['teacher'] = session['uname']
    print(question)
    questions.append(question)
    print(class_name_q2)
    
    question = {}
    
    print(''+question3)
    list_super_class =[]
    for cn in class_name_q2:
        c = JClass(session['uname']+"."+cn)() 
        super_c = c.getClass().getSuperclass().getSimpleName()
        list_super_class.append(super_c)
    super_class = [i for i in set(list_super_class) if i != "Object"]

    choice3 =[] 
    print(choice3)
    s = super_class
    super_str = ""
    print(s)
    for i in s:
        super_str = i

    choice3 = choiceSuperClassName(className , super_str)

    print(choice3)

    shuffle(choice3)
    print(choice3)
    correct_anws =[str(i) for i in super_class]
    question['question'] = question3
    question['Choice'] = choice3
    question['Correct_Ans'] = correct_anws
    question['teacher'] = session['uname']
    print(question)
    questions.append(question)

    question = {}
    
    print(''+ question4)
    sub_class = []
    for clasname in class_name_q2:
        
        c = JClass(session['uname']+"."+clasname)() 
        if(c.getClass().getSuperclass().getSimpleName() != "Object" and clasname not in sub_class):
            sub_class.append(clasname)    
    
    s = sub_class
    print(s)
    sub_class_str = ''
    for i in s:
        if(len(s) != count+1):
            sub_class_str += i+" "
            count += 1
        else:
            sub_class_str += i
    choice4 = choiceMultiClassName(className, sub_class_str)
    shuffle(choice4)
    print(choice4)
    question['question'] = question4
    question['Choice'] = choice4
    question['Correct_Ans'] = sub_class_str
    question['teacher'] = session['uname']
    print(question)
    questions.append(question)

    question ={}
    
    print(''+ question5)
    att_num = 0
    for i in class_name_q2:
        c = JClass(session['uname']+"."+i)() 
        attribute = c.getClass().getDeclaredFields()
        att_num += len(attribute)
    choice5 = choiceNumber(att_num)
    
    shuffle(choice5)
    print(choice5)
    question['question'] = question5
    question['Choice'] = choice5
    print('ตอบ: ' +str(att_num))
    question['Correct_Ans'] = str(att_num)
    question['teacher'] = session['uname']
    print(question)
    questions.append(question)


    question ={}
    
    print(''+ question6)
    p = len(attname)
    choice6 = choiceNumber(p)
    
    
    print(choice6)
    shuffle(choice6)
    print(choice6)
    question['question'] = question6
    question['Choice'] = choice6
    print('ตอบ: ' +str(p))
    question['Correct_Ans'] = p
    question['teacher'] = session['uname']
    print(question)
    questions.append(question)


    question ={}
    
    print(''+question7)
    for i in methods:
        
        m_name = str(i).replace(session['uname']+'.'+str(classname)+".",'')
        m_str_1 = m_name.replace('java.lang.String' , 'String')
        print(m_str_1)
    
    
    s = m_str_1
   
    choice8 = choiceMethodsName8(className,str(classname),s)
    shuffle(choice8)

    question['question'] = question7
    question['Choice'] = choice8
    question['Correct_Ans'] = m_str_1
    question['teacher'] = session['uname']
    print(question)
    questions.append(question)


    #q9 = "ผลลัพธ์จากโปรแกรมนี้ได้จะออกมาเป็นแบบไหน"
    #dic['question'] = q9
    #print('ข้อ 9 '+q9)
    #mc = JClass('j.MainClass').main([])   
    
    question = {}
    
    print(''+question8)
    print(len(cons))
    choice10 = choiceNumber(len(cons))
    
    
    print(choice10)
    shuffle(choice10)
    print(choice10)
    question['question'] = question8
    question['Choice'] = choice10
    print('ตอบ: ' +str(len(cons)))
    question['Correct_Ans'] = str(len(cons))
    question['teacher'] = session['uname']
    print(question)
    questions.append(question)
    
    question = {}
    
    print(''+question9)
    dic2 = collections.defaultdict(list)
    for i in class_name_q2:
        c = JClass(session['uname']+"."+i)() 
        methods_q11 = c.getClass().getDeclaredMethods()
        for j in methods_q11:
            m_str1 = str(j).replace(session['uname']+'.'+i+".",'')
            m_str2 = m_str1.replace('java.lang.String','String')
            dic2[str(c.getClass().getSimpleName())].append(m_str2)
    current_method = []
    overrideMethod = []  
    for i in dic2:
        if(len(current_method) == 0):
            current_method = dic2[i]
        else:
            for j in dic2[i]:
                if(j in current_method):
                    if(j not in overrideMethod):
                        overrideMethod.append(j)
            current_method = dic2[i]        
   
    choice11 = choiceMethodsName(className , overrideMethod[0])
    
    shuffle(choice11)
    print('--------------------')
    print(choice11)
    print('--------------------')
    question['question'] = question9
    question['Choice'] = choice11
    question['Correct_Ans'] = overrideMethod
    question['teacher'] = session['uname']
    print(question)
    questions.append(question)


    question = {}
    
    print(''+question10)
    correct_anwser = []
    for f in class_name_q2:
        sub_class = []
        c = JClass(session['uname']+"."+f)() 
        answer =[]
        if(c.getClass().getSuperclass().getSimpleName() != "Object"):
            answer.append(str(c.getClass().getSimpleName()))
            answer.append(str(c.getClass().getSuperclass().getSimpleName()))
        if(len(answer) != 0):
            correct_anwser.append(answer)  
    print(correct_anwser)
    choice12 = choiceClassRelationship(className)
    str_correct_anwser = str(correct_anwser)
    choice12.append(str_correct_anwser[1:len(str_correct_anwser)-1])
    shuffle(choice12)
    print(choice12)
    question['question'] = question10
    question['Choice'] = choice12
    question['Correct_Ans'] = str_correct_anwser[1:len(str_correct_anwser)-1]
    question['teacher'] = session['uname']
    print(question)
    questions.append(question)

    return questions

def generate_fill_in_the_bank(className ,question_fitb):
    questions = []
    question ={}
    anwser_all = []
    for cn in className:
        javaClass = JClass(session['uname']+"."+cn)()
        attname = javaClass.getClass().getDeclaredFields()
        constructor = javaClass.getClass().getDeclaredConstructors()
        methods = javaClass.getClass().getDeclaredMethods()
        anwser_all.append(str(javaClass.getClass().getSimpleName()))
        for attr in attname:
            
            if('java.lang.String' in str(attr)):
               anwser_all.append(str(attr).replace('java.lang.String '+session['uname']+'.'+str(cn)+'.' , 'String '))
            else:   
                anwser_all.append(str(attr).replace(session['uname']+'.'+str(cn)+".",''))
        for cons in constructor:
            
            if('java.lang.String' in str(cons)):
                strCons1 = str(cons).replace(session['uname']+'.','')
                strCons2 = strCons1.replace('java.lang.String','String')
                anwser_all.append(str(strCons2))
            else:
                anwser_all.append(str(cons).replace(session['uname']+'.',''))
        for method in methods:
            
            if('java.lang.String' in str(method)):
                strCons1 = str(method).replace(session['uname']+'.'+str(cn)+'.','')
                strCons2 = strCons1.replace('java.lang.String','String')
                anwser_all.append(str(strCons2))
            else:
                anwser_all.append(str(method).replace(session['uname']+'.'+str(cn)+".",''))
    #print(anwser_all)
    
    #question 1
    question['anwser_all'] = anwser_all
    question['teacher'] = session['uname']
    questions.append(question)
    question={}
    ran_class_name = className[randint(0,len(className)-1)]
    print(ran_class_name)
    q1_class = JClass(session['uname']+"."+ran_class_name)()
    question['question'] = question_fitb[0]['question'].replace('<classname>',str(ran_class_name))
    att_q1 = q1_class.getClass().getDeclaredFields()
    all_att_q1 =[]
    for attr in att_q1:
        if('java.lang.String' in str(attr)):
                all_att_q1.append(str(attr).replace('java.lang.String '+session['uname']+'.'+str(ran_class_name)+'.' , 'String '))
        else:
                all_att_q1.append(str(attr).replace(session['uname']+'.'+str(ran_class_name)+".",''))
    question['anwser'] = all_att_q1   
    question['teacher'] = session['uname']
    questions.append(question)
    print(question['anwser'])
  
    #question 2
    question={}
    ran_class_name = className[randint(0,len(className)-1)]
    q2_class = javaClass = JClass(session['uname']+"."+ran_class_name)()
    question['question'] = question_fitb[1]['question'].replace('<classname>',str(ran_class_name))
    cons_q2 = q2_class.getClass().getDeclaredConstructors()
    all_cons_q2 =[]
    for cons in  cons_q2:
            if('java.lang.String' in str(cons)):
                strCons1 = str(cons).replace(session['uname']+'.','')
                strCons2 = strCons1.replace('java.lang.String','String')
                all_cons_q2.append(str(strCons2))
            else:
                all_cons_q2.append(str(cons).replace(session['uname']+'.',''))
    question['anwser'] = all_cons_q2
    question['teacher'] = session['uname']
    questions.append(question)

    #question 3
    question={}
    question['question'] = question_fitb[2]['question'].replace('<classname>',str(ran_class_name))
    all_attr_q3 = []
    for cn in className:
        javaClass = javaClass = JClass(session['uname']+"."+cn)()
        attname = javaClass.getClass().getDeclaredFields()
        for attr in attname:
            if('private' in str(attr)):
                if('java.lang.String' in str(attr)):
                    all_attr_q3.append(str(attr).replace('java.lang.String '+session['uname']+'.'+str(cn)+'.' , 'String '))
                else:
                    all_attr_q3.append(str(attr).replace(session['uname']+'.'+str(cn)+".",''))
    question['anwser'] = all_attr_q3
    question['teacher'] = session['uname']
    questions.append(question)

    #question 4
    question={}
    question['question'] = question_fitb[3]['question'].replace('<classname>',str(ran_class_name))
    all_getter_methods = []
    for cn in className:
        javaClass = JClass(session['uname']+"."+cn)()
        methodName = javaClass.getClass().getDeclaredMethods()
        for method in methodName:
            if('get' in str(method)):
                if('java.lang.String' in str(method)):
                    all_getter_methods.append(str(method).replace('java.lang.String '+session['uname']+'.'+str(cn)+'.' , 'String '))
                else:
                    all_getter_methods.append(str(method).replace(session['uname']+'.'+str(cn)+".",''))
    question['anwser'] = all_getter_methods
    question['teacher'] = session['uname']
    questions.append(question)

    #question 5
    question={}
    question['question'] = question_fitb[4]['question'].replace('<classname>',str(ran_class_name))
    all_static_attr =[]
    for cn in className:
        javaClass = JClass(session['uname']+"."+cn)()
        attname = javaClass.getClass().getDeclaredFields()
        for attr in attname:
            if('static' in str(attr)):
                if('java.lang.String' in str(attr)):
                    all_static_attr.append(str(attr).replace('java.lang.String '+session['uname']+'.'+str(cn)+'.' , 'String '))
                else:
                    all_static_attr.append(str(attr).replace(session['uname']+'.'+str(cn)+".",''))
    question['anwser'] = all_static_attr
    question['teacher'] = session['uname']
    questions.append(question)

    #question 6
    question={}
    question['question'] = question_fitb[5]['question'].replace('<classname>',str(ran_class_name))
    all_setter_methods = []
    for cn in className:
        javaClass = JClass(session['uname']+"."+cn)()
        methodName = javaClass.getClass().getDeclaredMethods()
        for method in methodName:
            if('set' in str(method)):    
                if('java.lang.String' in str(method)):
                    strCons1 = str(method).replace(session['uname']+'.'+str(cn)+'.','')
                    strCons2 = strCons1.replace('java.lang.String','String')
                    all_setter_methods.append(strCons2)
                else:
                    all_setter_methods.append(str(method).replace(session['uname']+'.'+str(cn)+".",''))
    question['anwser'] = all_setter_methods
    question['teacher'] = session['uname']
    questions.append(question)

    return questions

def generate_question(question_q):
    question = {}
    questions =[]
    q1 = question_q[0]['question']
    question['question'] = q1
    question['teacher'] = session['uname']
    questions.append(question)
    question = {}
    q2 =question_q[1]['question']
    question['question'] = q2
    question['teacher'] = session['uname']
    questions.append(question)
    question = {}
    q3 =question_q[2]['question']
    question['question'] = q3
    question['teacher'] = session['uname']
    questions.append(question)
    question = {}
    q4 =question_q[3]['question']
    question['question'] = q4
    question['teacher'] = session['uname']
    questions.append(question)
    question = {}
    q5 =question_q[4]['question']
    question['question'] = q5
    question['teacher'] = session['uname']
    questions.append(question)
    question = {}
    q6 =question_q[5]['question']
    question['question'] = q6
    question['teacher'] = session['uname']
    questions.append(question)
    question = {}
    q7 =question_q[6]['question']
    question['question'] = q7
    question['teacher'] = session['uname']
    questions.append(question)
    question = {}
    q8 =question_q[7]['question']
    question['question'] = q8
    question['teacher'] = session['uname']
    questions.append(question)

    return questions