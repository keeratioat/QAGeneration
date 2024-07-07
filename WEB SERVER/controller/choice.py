from flask import session
from random import randint
from jpype import JClass
def choiceNumber(correct_ans):
    new_r = []
    new_r.append(correct_ans)
    i = 1
    while( i <= 3 ):
        r = randint(0, 8)
        if( r not in new_r ):
            new_r.append( r )
            i = i + 1
    return new_r     


def choiceMultiClassName(className,correct_awns):
    word_of_q = []
    word_class=['Triangle Circle','Department Employees','Airplane Boat Car','Animal Dog Cat']
    word_of_q.append(correct_awns)
   
    print(correct_awns)
    for i in range(len(className) - 1):
        word_class.append(className[i])
    
    i = 0
    while(i < 3):
        r = randint(0 , len(word_class) - 1)
        if(word_class[r] not in word_of_q):
            word_of_q.append(word_class[r])
            i+=1
    print('---------------')
    print(word_of_q) 
    print('---------------')          
    return word_of_q

def choiceSuperClassName(className,str_super):
    word_of_q = []
    word_class=['Triangle','Employees','Circle']
    word_of_q.append(str(str_super))
    for i in className:
        word_class.append(i)
    
    i = 0
    while(i < 3):
        r = randint(0 , len(word_class) - 1)
        if(word_class[r] not in word_of_q):
            word_of_q.append(word_class[r])
            i+=1           
    return word_of_q

def choiceMethodsName(className,correct_aws):
    word_of_q= ['public void calculate()' , 'private void showAllEmployee()']
    method_1 =[]
    method_2 =[]
    method_2.append(correct_aws)
    dicts2 = {}
    i = 1
    
    for cn in className:
        method = JClass(session['uname']+"."+cn)().getClass().getDeclaredMethods()
        for m in method: 
            str_m1 = str(m).replace('java.lang.String' , 'String')
            str_m2 = str_m1.replace(session['uname']+"."+cn+'.' , '')
            method_1.append(str(str_m2))
    for method in method_1:
        if(method not in word_of_q):
            word_of_q.append(str(method))
    while( i <= 3 ):
        r = randint(0,len(word_of_q)-1)
        if(word_of_q[r] not in method_2):
            method_2.append(str(word_of_q[r]))
            i+=1
    return method_2

def choiceMethodsName8(className ,classname ,correct_awns):
    word_of_q= ['public void calculate()' , 'private void showAllEmployee()']
    method_1 =[]
    method_2 =[]
    method_2.append(correct_awns)
    dicts2 = {}
    i = 1
    print(className)
    for cn in className:
        
        if(cn != classname):
            
            method = JClass(session['uname']+"."+cn)().getClass().getDeclaredMethods()
            for m in method: 
                str_m1 = str(m).replace('java.lang.String' , 'String')
                str_m2 = str_m1.replace(session['uname']+"."+cn+'.' , '')
                method_1.append(str(str_m2))
    for method in method_1:
        if(method not in word_of_q):
            word_of_q.append(str(method))
    while( i <= 3 ):
        r = randint(0,len(word_of_q)-1)
        if(word_of_q[r] not in method_2):
            method_2.append(str(word_of_q[r]))
            i+=1
    return method_2

def choiceClassRelationship(className):
    word_of_q_1 = ['Fruit' , 'Orenge' ,'Banana','Apple']
    word_of_q_2 = []
    word_of_q_3 =[]

    for i in className:
      word_of_q_1.append(i)
    i=0
    while i < 3:
        word_of_q_2 = []
        j = 0
        while  j < 2:
            r = randint(0,len(word_of_q_1)-1)
            if(word_of_q_1[r] not in word_of_q_2):
              word_of_q_2.append(str(word_of_q_1[r]))
              j+=1
              word_of_q_2.sort()
        if( str(word_of_q_2) not in word_of_q_3):
          word_of_q_3.append(str(word_of_q_2))
          i+=1
    return word_of_q_3