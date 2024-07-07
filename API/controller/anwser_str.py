def correct_anwser_str(correct_aws):
    if(str(type(correct_aws)) == "<class 'list'>"):
                count = 0
                correct_ans =""
                for j in correct_aws:
                    if(str(type(j)) != "<class 'list'>"):
                        if(len(correct_aws) != count+1):
                            correct_ans += j+" "
                            count += 1
                        else:
                            correct_ans += j
                    
                return correct_ans
    else:
        return correct_aws
                
def choice_str(choice):
        for c in choice:    
            #print(type(c))        
            if(str(type(c)) == "<class 'list'>"):
                count = 0
                correct_ans =""
                for j in c:
                    
                    if(str(type(j)) != "<class 'list'>"):
                        if(len(c) != count+1):
                            correct_ans += j+" "
                            count += 1
                        else:
                            correct_ans += j
                    
                
                choice.remove(c)
                choice.append(correct_ans)
        return choice       
