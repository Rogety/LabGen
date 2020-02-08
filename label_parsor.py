# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
from argparse import ArgumentParser
from copy import copy, deepcopy
import os

## lab 外部輸入

##"arctic_a0001"


def load_sentence(label):
    #input : label in cmu_us_arctic_slt
    #output : sentence including punctuation and transform to upper
    # print("\t\t\t load_sentence \t\t\t")
    DEBUG_MODE = 0
    
    f = open('arctic_sentense.txt', 'r+')
    for line in f :
        if re.search("[a-z]\d{4}" , in_label).group(0) == re.search("[a-z]\d{4}" , line).group(0):
            pattern = r"\".*\""
            sentence = re.search(pattern , line).group(0).strip('"')
            break
        
    sentence = sentence.strip(" ")

    if sentence.find("etc") != -1:
        sentence.replace("etc" , "etcetera")
        
    f.close()
    
    if DEBUG_MODE == 1:
        print("function : load_sentence(label)")
        print("sentence =",sentence)
        
    return  sentence




def load_lab(label):
    # print("\t\t\t load_lab \t\t\t")
    ##input : label in cmu_us_arctic_slt
    ##output : Start,End,P_LAB,B_LAB,E_LAB
    '''
    Start : strat time
    end : end time
    P_LAB : phoneme
    B_LAB :
    E_LAB : POS
    '''
    
    DEBUG_MODE = 0
    
    Start , End =[],[]
    P_LAB,A_LAB,B_LAB,C_LAB,D_LAB,E_LAB,F_LAB,G_LAB,H_LAB,I_LAB,J_LAB=[],[],[],[],[],[],[],[],[],[],[]
    f = open("./lab/" + label, 'r+')
    '''
    for line in f :
        start_time = re.findall(r" \d+ " , line)[0].strip(" ")
        end_time = re.findall(r" \d+ " , line)[1].strip(" ")
        P = re.findall(r"[a-z]+\^[a-z]+\-[a-z]+\+\w+\=\w+\@\w+\_\w+" , line)[0]
        A = re.findall(r"\/A\:[0-9]\_[0-9]\_[0-9]",line)[0]
        B = re.findall(r"\/B\:\w\-\w\-\w\@\w\-\w\&\w-\w#\w-\w\$\w-\w!\w-\w;\w-\w\|\w",line)[0]
        C = re.findall(r"\/C\:\w\+\w\+\w",line)[0]
        D = re.findall(r"\/D\:\w+\_\w",line)[0]
        E = re.findall(r"\/E\:\w+\+\w\@\w\+\w\&\w\+\w\#\w\+\w",line)[0]
        F = re.findall(r"\/F\:\w+_\w",line)[0]
        G = re.findall(r"\/G\:\w_\w",line)[0]
        H = re.findall(r"\/H\:\w\=\w\^\w\=\w\|\w",line)[0]
        I = re.findall(r"\/I\:\w\=\w",line)[0]
        J = re.findall(r"\/J\:\w+\+\w+\-\w",line)[0]
        
        P_G = re.search(r"(.*)\^(.*)\-(.*)\+(.*)\=(.*)\@(.*)\_(.*)" , P )
        A_G = re.search(r"\/A\:(.*)\_(.*)\_(.*)" , A)
        B_G = re.search(r"\/B\:(.*)\-(.*)\-(.*)\@(.*)\-(.*)\&(.*)\-(.*)\#(.*)\-(.*)\$(.*)\-(.*)\!(.*)\-(.*)\;(.*)\-(.*)\|(.*)" , B)
        C_G = re.search(r"\/C\:(.*)\+(.*)\+(.*)" , C)
        D_G = re.search(r"\/D\:(.*)\_(.*)" , D)
        E_G = re.search(r"\/E\:(.*)\+(.*)\@(.*)\+(.*)\&(.*)\+(.*)\#(.*)\+(.*)" , E)
        F_G = re.search(r"\/F\:(.*)\_(.*)" , F)
        G_G = re.search(r"\/G\:(.*)\_(.*)" , G)
        H_G = re.search(r"\/H\:(.*)\=(.*)\^(.*)\=(.*)\|(.*)" , H)
        I_G = re.search(r"\/I\:(.*)\=(.*)" , I)
        J_G = re.search(r"\/J\:(.*)\+(.*)\-(.*)" , J)
        
        
        P_7 = [P_G.group(0),P_G.group(1),P_G.group(2),P_G.group(3),P_G.group(4),P_G.group(5),P_G.group(6),P_G.group(7)]
        A_3 = [A_G.group(0),A_G.group(1),A_G.group(2),A_G.group(3)]
        B_16 = [B_G.group(0),B_G.group(1),B_G.group(2),B_G.group(3),B_G.group(4),B_G.group(5),B_G.group(6),B_G.group(7),B_G.group(8),
                B_G.group(9),B_G.group(10),B_G.group(11),B_G.group(12),B_G.group(13),B_G.group(14),B_G.group(15),B_G.group(16)]
        C_3 = [C_G.group(0),C_G.group(1),C_G.group(2),C_G.group(3)]
        D_2 = [D_G.group(0),D_G.group(1),D_G.group(2)]
        E_8 = [E_G.group(0),E_G.group(1),E_G.group(2),E_G.group(3),E_G.group(4),
               E_G.group(5),E_G.group(6),E_G.group(7),E_G.group(8),]
        F_2 = [F_G.group(0),F_G.group(1),F_G.group(2)]
        G_2 = [G_G.group(0),G_G.group(1),G_G.group(2)]
        H_5 = [H_G.group(0),H_G.group(1),H_G.group(2),H_G.group(3),H_G.group(4),H_G.group(5)]
        I_2 = [I_G.group(0),I_G.group(1),I_G.group(2)]
        J_3 = [J_G.group(0),J_G.group(1),J_G.group(2),J_G.group(3)]
        
        Start.append(start_time)
        End.append(end_time)
        P_LAB.append(P_7)
        A_LAB.append(A_3)
        B_LAB.append(B_16)
        C_LAB.append(C_3)
        D_LAB.append(D_2)
        E_LAB.append(E_8)
        F_LAB.append(F_2)
        G_LAB.append(G_2)
        H_LAB.append(H_5)
        I_LAB.append(I_2)
        J_LAB.append(J_3)
        #print(line)
    '''
    for line in f :
        #print(line)
        start_time = re.findall(r" \d+ " , line)[0].strip(" ")
        end_time = re.findall(r" \d+ " , line)[1].strip(" ")
        P = re.findall(r"[a-z]+\^[a-z]+\-[a-z]+\+\w+\=\w+\@\w+\_\w+" , line)[0]
        B = re.findall(r"\/B\:\w\-\w\-\w\@\w\-\w\&\w*-\w*#\w*-\w*\$\w-\w!\w-\w;\w*-\w*\|\w",line)[0]
        E = re.findall(r"\/E\:\w+\+\w\@\w*\+\w*\&\w\+\w\#\w\+\w",line)[0]
        
        P_G = re.search(r"(.*)\^(.*)\-(.*)\+(.*)\=(.*)\@(.*)\_(.*)" , P )
        B_G = re.search(r"\/B\:(.*)\-(.*)\-(.*)\@(.*)\-(.*)\&(.*)\-(.*)\#(.*)\-(.*)\$(.*)\-(.*)\!(.*)\-(.*)\;(.*)\-(.*)\|(.*)" , B)
        E_G = re.search(r"\/E\:(.*)\+(.*)\@(.*)\+(.*)\&(.*)\+(.*)\#(.*)\+(.*)" , E)
        
        P_G = re.search(r"(.*)\^(.*)\-(.*)\+(.*)\=(.*)\@(.*)\_(.*)" , P )
        B_G = re.search(r"\/B\:(.*)\-(.*)\-(.*)\@(.*)\-(.*)\&(.*)\-(.*)\#(.*)\-(.*)\$(.*)\-(.*)\!(.*)\-(.*)\;(.*)\-(.*)\|(.*)" , B)
        E_G = re.search(r"\/E\:(.*)\+(.*)\@(.*)\+(.*)\&(.*)\+(.*)\#(.*)\+(.*)" , E)
        
        P_7 = [P_G.group(0),P_G.group(1),P_G.group(2),P_G.group(3),P_G.group(4),P_G.group(5),P_G.group(6),P_G.group(7)]
        B_16 = [B_G.group(0),B_G.group(1),B_G.group(2),B_G.group(3),B_G.group(4),B_G.group(5),B_G.group(6),B_G.group(7),B_G.group(8),
                B_G.group(9),B_G.group(10),B_G.group(11),B_G.group(12),B_G.group(13),B_G.group(14),B_G.group(15),B_G.group(16)]
        E_8 = [E_G.group(0),E_G.group(1),E_G.group(2),E_G.group(3),E_G.group(4),
               E_G.group(5),E_G.group(6),E_G.group(7),E_G.group(8)]
        
        Start.append(start_time)
        End.append(end_time)
        P_LAB.append(P_7)
        B_LAB.append(B_16)
        E_LAB.append(E_8)
 

    f.close()
    
    
    
    # if DEBUG_MODE == 1:
    #     print("funciotn : load_lab(label)")
    #     print("Start =",Start)
    #     print("End =",End)
    #     print("P_LAB =",P_LAB)
    #     print("B_LAB =",B_LAB)
    #     print("E_LAB =",E_LAB)
        
        
    #return Start,End,P_LAB,A_LAB,B_LAB,C_LAB,D_LAB,E_LAB,F_LAB,G_LAB,H_LAB,I_LAB,J_LAB
    return Start,End,P_LAB,B_LAB,E_LAB 


def generate_mul(Start,End,P_LAB,B_LAB,E_LAB,in_label,
                 syl_start,word_start,word_dict,word_list,syllable_list,stress_phone,stress_class,phone_list_pau,
                 phone_before_comma,phone_before_period,phone_before_semicolon,phone_after_comma,phone_after_period,phone_after_semicolon):
    # print("\t\t\t generate_mul \t\t\t")
    title = in_label.rstrip(".lab")
    
    folder = os.path.exists("./mul/")
    if not folder:
        os.makedirs("./mul/")

    w = open( './mul/' + title + '.mul','w+')
    k=0
    m=0

    
    ##get stress index
    stress_index = []
    n=0
    for i in range(len(phone_list_pau)):
        if n < len(stress_phone):
            #print(stress_phone[n] , phone_list_pau[i])
            if stress_phone[n].startswith(phone_list_pau[i]):
                stress_index.append(i)
                n=n+1
    # print(Start[0:5])
    # print(End[0:5])
    
    # print(len(phone_list_pau) , len(Start))
    
    ## 合併切割時間
    if len(phone_list_pau) != len(Start) and len(Start)-len(phone_list_pau)==1:
        End[0] = Start[2]
        del Start[1]
        del End[1]
        
    # print("比對phone(含pau)的數量 和 切割時間的數量",len(phone_list_pau) , len(Start))   ##比對phone_list的數量 和 切割時間的數量 
    # print("stress數量和syllable數量",len(stress_index) , len(syl_start)) ##比對strees的數量 和 syllable的數量
    # print(phone_list_pau)
    for i in range(0,len(phone_list_pau)):
        w.write("{}".format(Start[i]) )
        w.write(" ")
        w.write("{}".format(End[i]) )
        w.write(" ")
        w.write("{}".format(phone_list_pau[i]))
        w.write(" ")
        #print(i , B_LAB[i][1])
        
        
        if k < len(stress_index):
            if i == syl_start[k]:
                w.write("{}".format(stress_class[k]))
                w.write(" ")
                k=k+1
            
        
        if i == word_start[m] :
            w.write("{}".format(word_dict[word_list[m]]))
            w.write(" ")
            ## POS
            if E_LAB[i][1] != 'x':
                w.write("{}".format("1"))
                w.write(" ")
                w.write("{}".format(E_LAB[i][1]))
                w.write(" ")
                

            if word_dict[word_list[m]] in phone_before_comma :
                w.write("{}".format("1"))
                w.write(" ")
                w.write("{}".format(","))
                w.write(" ")
            elif word_dict[word_list[m]] in phone_before_period :
                w.write("{}".format("1"))
                w.write(" ")
                w.write("{}".format("."))
                w.write(" ")
            elif word_dict[word_list[m]] in phone_before_semicolon :
                w.write("{}".format("1"))
                w.write(" ")
                w.write("{}".format(";"))
                w.write(" ")
            else:
                w.write("{}".format("0"))
                w.write(" ")
            if word_dict[word_list[m]] in phone_after_comma :
                w.write("{}".format("1"))
                w.write(" ")
                w.write("{}".format(","))
                w.write(" ")
            elif word_dict[word_list[m]] in phone_after_period :
                w.write("{}".format("1"))
                w.write(" ")
                w.write("{}".format("."))
                w.write(" ")
            elif word_dict[word_list[m]] in phone_after_semicolon :
                w.write("{}".format("1"))
                w.write(" ")
                w.write("{}".format(";"))
                w.write(" ")
            else:
                w.write("{}".format("0"))
                w.write(" ")
                
                

            
                
            m=m+1
            if m == len(word_start):
                m=0
        
        w.write("\n")
    w.close()
    
    # print("phone_list_pau =",phone_list_pau,len(phone_list_pau))
    # print("word_list =",word_list,len(word_list))
    # print("syllable_list =",syllable_list,len(syllable_list))
    # print("stress_phone =",stress_phone ,len(stress_phone))
    # print("stress_index =",stress_index , len(stress_index))
    # print("stress_class =",stress_class ,len(stress_class))
    # print("syl_start =",syl_start,len(syl_start))
    # print("word_start =",word_start,len(word_start))
    # print("word_dict =",word_dict)
    
    
    if len(phone_list_pau) != len(Start):
        
        folder = os.path.exists("./log/")
        if not folder:
            os.makedirs("./log/")

        w = open( './log/' + title + '.mul','w+')
        w.write(str(len(phone_list_pau)))
        w.write('\t')
        w.write(str(len(Start)))
        w.close()
        

def specail_case_processing(word_list):
    # print("\t\t\t specail_case_processing \t\t\t")
    if "iht" in word_list and "s" in word_list \
        and (word_list.index("iht") - word_list.index("s") == -1):
        n = word_list.index("iht")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"ihts")
    ## there's
    if "dhehr" in word_list and "z" in word_list \
        and (word_list.index("dhehr") - word_list.index("z") == -1):
        n = word_list.index("dhehr")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"dhehrz")        
    if "ahdher" in word_list and "z" in word_list:
        n = word_list.index("ahdher")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"ahdherz")    
    if "piyehr" in word_list and "z" in word_list:
        n = word_list.index("piyehr")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"piyehrz")      
    if "fihlaxp" in word_list and "s" in word_list:
        n = word_list.index("fihlaxp")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"fihlaxps")  
    if "faadher" in word_list and "z" in word_list:
        n = word_list.index("faadher")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"faadherz")      
    if "dhaet" in word_list and "s" in word_list:
        n = word_list.index("dhaet")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"dhaets") 
    if "leht" in word_list and "s" in word_list:
        n = word_list.index("leht")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"lehts")     
    if "gerl" in word_list and "z" in word_list:
        n = word_list.index("gerl")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"gerlz")  
    if "ay" in word_list and "z" in word_list \
        and (word_list.index("ay") - word_list.index("z") == -1):
        n = word_list.index("ay")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"ayz")      
    if "layf" in word_list and "s" in word_list:
        n = word_list.index("layf")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"layfs")    
    if "neym" in word_list and "z" in word_list:
        n = word_list.index("neym")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"neymz")   
    if "hhihr" in word_list and "z" in word_list:
        n = word_list.index("hhihr")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"hhihrz")     
    if "hhiy" in word_list and "z" in word_list \
        and (word_list.index("hhiy") - word_list.index("z") == -1):
        n = word_list.index("hhiy")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"hhiyz")        
    if "maen" in word_list and "z" in word_list:
        n = word_list.index("maen")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"maenz") 
    if "paekerd" in word_list and "z" in word_list:
        n = word_list.index("paekerd")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"paekerdz")         
    if "taxdey" in word_list and "z" in word_list:
        n = word_list.index("taxdey")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"taxdeyz")  
    if "waht" in word_list and "s" in word_list:
        n = word_list.index("waht")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"wahts")   
    if "saeksaxn" in word_list and "z" in word_list:
        n = word_list.index("saeksaxn")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"saeksaxnz")       
    if "hhuw" in word_list and "z" in word_list:
        n = word_list.index("hhuw")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"hhuwz")       
    if "skihper" in word_list and "z" in word_list:
        n = word_list.index("skihper")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"skihperz")   
    if "sehldaxn" in word_list and "z" in word_list:
        n = word_list.index("sehldaxn")
        del word_list[n]
        del word_list[n]
        word_list.insert(n,"sehldaxnz")           
    
        
        
    return word_list
        
    
        
def generate_label_ref(B_LAB,P_LAB):    
    # print("\t\t\t generate_label_ref \t\t\t")
    
    syl_start , syl_count , word_start , word_count = [],[],[],[]
    syl_list , word_list = [],[]
    # b3 : the number of phonemes in the current syllable
    # b4 : position of the current syllable in the current word (forward)
    # b5 : position of the current syllable in the current word (backward)
    
    # syl_start + 1 = 行數
    
    i=0
    #print(B_LAB)
    while i < len(B_LAB):
        if (B_LAB[i][3] != 'x'):
            syl_start.append(i)
            syl_count.append(int(B_LAB[i][3]))
            if B_LAB[i][4] == '1':
                word_start.append(i)
                word_count.append(int(B_LAB[i][5]))
                
            i = i + int(B_LAB[i][3]) 
        else:
            i = i+1
            
    #print("syl_start = ",syl_start)
    #print("syl_count = ",syl_count)
    #print("word_start = ",word_start)
    #print("word_count = ",word_count)
    

    for i in range(0,len(syl_start)):  
        j=0
        s=""
        while j < syl_count[i]:
            s += P_LAB[ syl_start[i] + j ][3]
            #print(P_LAB[ syl_start[i] + j ][3], end="")
            j=j+1
        syl_list.append(s)
        
    # print(syl_list , len(syl_list))   
    i=0
    k=0
    while i < len(word_count):
        j=0
        s=""
        while j < word_count[i]:
            s += syl_list[k+j]
            j=j+1
        k += j
        word_list.append(s)        
        i += 1
        
    # print(word_list , len(word_list)) 
    
    
    ##specail case processing 
    ## "It's"
    
    #word_list_ref = specail_case_processing(word_list)
    word_list_ref = word_list
    
    # syl_sentense = ' '.join(syl_list)
    word_sentense_ref = ' '.join(word_list_ref)
    word_list_ref = word_list_ref
    
    #print(syl_list)   
    #print(syl_sentense)
    #print(word_list)
    #print(word_sentense)
    # if DEBUG_MODE == 1:
    #     print("function : generate_label_ref(B_LAB,P_LAB)")
    #     print("word_sentense_ref =",word_sentense_ref)
    #     print("word_list_ref =",word_list_ref)
    

    return word_sentense_ref , word_list_ref

    
def phone_mapping(word_sentense , original_sentense ):
    # print("\t\t\t phone_mapping \t\t\t")
    #print("'''''''''''''''''phone_mapping'''''''''''''''''''''''''")
    word_dict ={}
    original_sentense = original_sentense.replace(",","")
    original_sentense = original_sentense.replace(".","")
    original_sentense = original_sentense.replace(";","")
    original_list = original_sentense.split(" ")
    word_list = word_sentense.replace("ax","ah").split(" ")

    for i in range(len(word_list)):
        word_dict[word_list[i].upper()] = original_list[i]

    
    
    return word_dict

def comma_phone(sentence):
    # print("\t\t\t comma_phone \t\t\t")
    phone_before_comma = []
    phone_before_period = []
    phone_before_semicolon = []
    phone_after_comma = []
    phone_after_period = []    
    phone_after_semicolon = []
    
    sentence = sentence.replace(","," ,")
    sentence = sentence.replace("."," .")
    sentence = sentence.replace(";"," ;")
    sentence_list = sentence.split(" ")

    for i in range(len(sentence_list)):
        if sentence_list[i] == ',':
            phone_before_comma.append(sentence_list[i-1])
            if i != len(sentence_list)-1:
                phone_after_comma.append(sentence_list[i+1])
        if sentence_list[i] == ';':
            phone_before_semicolon.append(sentence_list[i-1])
            if i != len(sentence_list)-1:
                phone_after_semicolon.append(sentence_list[i+1])
        if (sentence_list[i] == '.') :
            phone_before_period.append(sentence_list[i-1])
            if i != len(sentence_list)-1: ## avoid list index out of range
                phone_after_period.append(sentence_list[i+1])
    

                
    return phone_before_comma,phone_before_period,phone_before_semicolon,phone_after_comma,phone_after_period,phone_after_semicolon
    


def get_syllable_info(sentense , plabel , word_list_ref , word_sentense):
    # print("\t\t\t get_syllable_info \t\t\t")    

    # print("sentense =",sentense)
    sentense = sentense.replace(",","")
    sentense = sentense.replace(".","")
    sentense = sentense.replace(";","")
    sentense = sentense.replace("-"," ")
    sentense = sentense.replace("'s"," 's")
    sentense = sentense.replace("1908","19 0 8")
    sentense = sentense.replace("29th","29 th")
    sentense_list = sentense.split(" ")
    # print("sentense_list =",sentense_list)
    
    #line = 'SHARPLY sh aa1 r p - l iy0'

    #coword = re.findall('[A-Z]+' , line)[0]
    #print(coword)
    

    text = get_syllable_text()    
    
    
    ##get phone_label
    phone_label = []
    for i in range(len(plabel)):
        phone_label.append(plabel[i][3])
    while 'pau' in phone_label:
        phone_label.remove('pau')
    #print('phone_label = ',phone_label , len(phone_label))   

    
    ## for worlist ax->ah
    wordlist_tmp = [] 
    for item in word_list_ref:
        wordlist_tmp.append(item.replace("ax" , "ah"))
    #print('word_list =' ,word_list_ref )
    
    phone_list = []
    syllable_list =[]
    stress_phone = []
    stress_index = []
    word_list = []
    
    
    ##get phone and syllable
    # print("wordlist_tmp = ",wordlist_tmp)
    i=0
    for word in sentense_list:
        #print(word)    
        line_list = []

        
        word = word.upper()
        word_list.append(word.lower())
        cmp = ""
        # print("word",word)
        for line in text:
            
            if i == len(wordlist_tmp):
                break
            
            flag = 0
            line_text = line.split(" ")
            if line.find(word) != -1 and line.startswith(word) and (len(word) == len(line_text[0])):
                
                # print(line)
                #print(line)
                line = line.lstrip(word)
                line = line.strip()
                #print("line = ",line)
                cmp = line.replace("0","")
                cmp = cmp.replace("1","")
                cmp = cmp.replace("2","")
                cmp = cmp.replace(" ", "")    
                cmp = cmp.replace("-","")
                cmp = cmp.replace("ah","ax")
                cmp = cmp.lower()

                # print('cmp =',cmp , wordlist_tmp[i])
                if  cmp == wordlist_tmp[i]:
                    #print('cmp =',cmp , wordlist_tmp[i])
                    i = i+1
                    flag = 1
                
                if flag==1:
                    line_list = line.split(" ")
                   #print("line_list =",line_list)
                    for item in line_list:
                        phone_list.append(item)
                    syllable_list.append(line_list)
                    
    ##  rmove '-' in phone_list                    
    while '-' in phone_list:
        phone_list.remove('-')
        
    #print("phone_list =",phone_list , len(phone_list))
    #print("syllable_list =",syllable_list)

    

    
    ##get stress info
    for item in phone_list:
        if item.isalpha() != 1:
            ph = re.findall(r"[a-zA-Z]+" , item)[0]
            stress = re.findall(r"\d+" , item)[0]
            #print(item , ph , stress)
            stress_phone.append(ph)
            stress_index.append(stress)
    
    #print("stress_phone = ",stress_phone , len(stress_phone))
    #print("stress_index = ",stress_index , len(stress_index))
    
    

    
    
    tmp = []
    tmp1 = deepcopy(syllable_list) 
    tmp3 = deepcopy(syllable_list)
    tmp2 = []
    syl_list = []
    word_phone_list=[]
    ph_num_in_word = [] 
    ph_num_in_syllable = []
    ##get phone num in syllable
    for item in tmp3:  
        if '-' in item:
            item = "+".join(item)
            item = item.split("-")    
            for element in item:
                b = element.split("+")
                b = list(filter(None, b)) 
                ph_num_in_syllable.append(len(b))            
        else:
            ph_num_in_syllable.append(len(item))
            
    #print("ph_num_in_syllable =",ph_num_in_syllable ,len(ph_num_in_syllable))
    
    
    
    ##get phone num in word
    
    for item in tmp1:
        while '-' in item:
            item.remove('-')
        ph_num_in_word.append(len(item))

    #print("ph_num_in_word =",ph_num_in_word ,len(ph_num_in_word))
        
    ##sort phone_list
    for i in range(len(phone_list)):
        ph = re.findall(r"[a-zA-Z]+" , phone_list[i])[0]
        phone_list[i] = ph
    #print("phone_list = ",phone_list)
    
    #print("syllable_list = ",syllable_list)
    ##sort syllable_list
    for item in syllable_list:
        tmp.append("".join(item))
        
    #print("tmp = ",tmp)
    for item in tmp:
        item = item.replace("0","")
        item = item.replace("1","")
        item = item.replace("2","")
        tmp2.append(item)
        
    for item in tmp2:
        if item.find("-") != -1:
            ch = item.split("-")
            for item2 in ch:
                syl_list.append(item2)
        else:
            syl_list.append(item)
            
    #print("syl_list = ",syl_list)
    ## create word_phone_list        
    for item in tmp2:
        word_phone_list.append(item.replace('-',''))
        
        
    word_dict = phone_mapping(word_sentense , sentense)
    #print("tmp = " , tmp)
    #print("tmp2 = ",tmp2)
    #print("syl_list = ",syl_list)

    
    #rint("syllable_list = ",syl_list)
    # print("word_list = ",word_list)
    # print("word_phone_list = ",word_phone_list)
    # print("ph_num_in_word =",ph_num_in_word)
    # print("'''''''''''''''''end''''''''''''''''''''''")
    
    return phone_list,syl_list,word_list,word_phone_list,word_dict,stress_phone,stress_index,ph_num_in_word,ph_num_in_syllable
    

def get_syllable_text():
    # print("\t\t\t get_syllable_text \t\t\t")
    text = []
    f = open('bu_radio_dict_with_syl.txt', 'r+')
    for line in f:
        text.append(line)
    f.close()
    
    return text


def generate_stamp(B_LAB,P_LAB,phone_list,syllable_list,word_phone_list,ph_num_in_word,ph_num_in_syllable):

    # print("\t\t\t generate_stamp \t\t\t")
    P_label = []
    pau_index = []
    syl_start_index = []
    word_start_index = []
    
    for item in P_LAB:
        P_label.append(item[3])
        
    ##get pau index
    for i in range(len(P_label)):
        if P_label[i] =='pau':
            pau_index.append(i)
            
    # print("pau_index =",pau_index , len(phone_list))
    ## add PAU element to phone_list
    for i in range(len(pau_index)):
        
        if pau_index[i] == 0:
             phone_list.insert(0,'sil')     
             continue
        if pau_index[i] < 3 and (pau_index[i]-pau_index[i-1] == abs(1) ): ## magic number
             phone_list.insert(0,'sil')
             continue
        if pau_index[i] == len(phone_list):
             phone_list.insert(pau_index[i],'sil')
             continue
        phone_list.insert(pau_index[i],'sp')
        #print(len(phone_list))
        
    ## 把index = 1 的 pau 刪掉 
    if phone_list[1] == 'sil':
        del phone_list[1]
        

    # print("word_phone_list =",word_phone_list)
    # print("syllable_list =",syllable_list , len(syllable_list))
    # print("ph_num_in_syl =",ph_num_in_syllable ,len(ph_num_in_syllable))
    # print(phone_list)
    # print(ph_num_in_syllable)
    
    i,j,k=0,0,0
    while i < len(phone_list):
        #if phone_list[i] == 'PAU':
            #continue
        ##syllable
        if k < len(word_phone_list):
            if word_phone_list[k].startswith(phone_list[i]) and word_phone_list[k].endswith(phone_list[i+ph_num_in_word[k]-1]):
                word_start_index.append(i)
                k = k+1
        
        if j < len(syllable_list):
            #print(syllable_list[j] , phone_list[i] , phone_list[i+ph_num_in_syllable[j]-1] , ph_num_in_syllable[j])
            if syllable_list[j].startswith(phone_list[i]) and syllable_list[j].endswith(phone_list[i+ph_num_in_syllable[j]-1]) :
                # print(syllable_list[j] , phone_list[i] , phone_list[i+ph_num_in_syllable[j]-1])
                syl_start_index.append(i)
                i += ph_num_in_syllable[j]-1
                j = j+1
        
        i =i+1
        
       

            
    
    # print("syl_start_index = " , syl_start_index , len(syl_start_index))
    # print("word_start_index = " , word_start_index)
    # print("phone_list =",phone_list,len(phone_list))
    # print("syllable_list =",syllable_list)
    # print("word_phone_list =",word_phone_list)
    


    
    
    
    return phone_list , syl_start_index , word_start_index


if __name__ == '__main__':

    
    
    for dirPath, dirNames, fileNames in os.walk("./lab"):
        arctic_fileName = fileNames

    arctic_fileName = arctic_fileName[0:-1]
    
    # print(arctic_fileName)
    for fileNames in arctic_fileName :
        print("Generate " , fileNames.replace(".lab" , ".mul"))
        in_label = fileNames   
        sentence_load = load_sentence(in_label)
        #Start,End,P_LAB,A_LAB,B_LAB,C_LAB,D_LAB,E_LAB,F_LAB,G_LAB,H_LAB,I_LAB,J_LAB = load_lab(in_label)
        Start,End,P_LAB,B_LAB,E_LAB = load_lab(in_label)    
        word_sentense_ref , word_list_ref = generate_label_ref(B_LAB,P_LAB)  
        phone_list , syllable_list ,word_list,word_phone_list,word_dict, stress_phone , stress_class , ph_num_in_word , ph_num_in_syllable \
        = get_syllable_info(sentence_load , P_LAB , word_list_ref,word_sentense_ref)  
        phone_list_pau , syl_start_index , word_start_index = generate_stamp(B_LAB,P_LAB,phone_list,syllable_list,word_phone_list,ph_num_in_word,ph_num_in_syllable) 
        phone_before_comma,phone_before_period,phone_before_semicolon,phone_after_comma,phone_after_period,phone_after_semicolon = comma_phone(sentence_load)
        #generate_mul(Start,End,P_LAB,A_LAB,B_LAB,C_LAB,D_LAB,E_LAB,F_LAB,G_LAB,H_LAB,I_LAB,J_LAB,syl_start,word_start,word_dict,word_list,
        #             phone_before_comma,phone_before_period,phone_before_semicolon,phone_after_comma,phone_after_period,phone_after_semicolon)
        generate_mul(Start,End,P_LAB,B_LAB,E_LAB,in_label,syl_start_index,word_start_index,word_dict,word_phone_list,syllable_list,stress_phone,stress_class,phone_list_pau,
                     phone_before_comma,phone_before_period,phone_before_semicolon,phone_after_comma,phone_after_period,phone_after_semicolon)    
        

    '''
    
    fileNames = "cmu_us_arctic_slt_b0449.lab"
    in_label = fileNames   
    sentence_load = load_sentence(in_label)
    print("sentence_load =",sentence_load)
        #Start,End,P_LAB,A_LAB,B_LAB,C_LAB,D_LAB,E_LAB,F_LAB,G_LAB,H_LAB,I_LAB,J_LAB = load_lab(in_label)
    Start,End,P_LAB,B_LAB,E_LAB = load_lab(in_label)    
    word_sentense_ref , word_list_ref = generate_label_ref(B_LAB,P_LAB)  
    print("word_sentense_ref = ",word_sentense_ref)
    print("word_list_ref = ",word_list_ref)
    phone_list , syllable_list ,word_list,word_phone_list,word_dict, stress_phone , stress_class , ph_num_in_word , ph_num_in_syllable \
    = get_syllable_info(sentence_load , P_LAB , word_list_ref,word_sentense_ref)  
    print("phone_list =",phone_list,len(phone_list)," phone")
    print("syllable_list =",syllable_list,len(syllable_list)," syllable")
    print("word_list =",word_list,len(word_list)," word")
    print("word_phone_list =",word_phone_list)
    #print("word_dict =",word_dict)
    print("stress_phone =",stress_phone)
    print("stress_class =",stress_class,len(stress_class)," stress")
    print("ph_num_in_word =",ph_num_in_word)
    print("ph_num_in_syllable =",ph_num_in_syllable)
    
    phone_list_pau , syl_start_index , word_start_index = generate_stamp(B_LAB,P_LAB,phone_list,syllable_list,word_phone_list,ph_num_in_word,ph_num_in_syllable) 
    print("phone_list_pau =",phone_list_pau,len(phone_list_pau)," phone(pau)")
    print("syl_start_index =",syl_start_index)
    print("word_start_index =",word_start_index)
    phone_before_comma,phone_before_period,phone_before_semicolon,phone_after_comma,phone_after_period,phone_after_semicolon = comma_phone(sentence_load)
        #generate_mul(Start,End,P_LAB,A_LAB,B_LAB,C_LAB,D_LAB,E_LAB,F_LAB,G_LAB,H_LAB,I_LAB,J_LAB,syl_start,word_start,word_dict,word_list,
        #             phone_before_comma,phone_before_period,phone_before_semicolon,phone_after_comma,phone_after_period,phone_after_semicolon)
    generate_mul(Start,End,P_LAB,B_LAB,E_LAB,in_label,syl_start_index,word_start_index,word_dict,word_phone_list,syllable_list,stress_phone,stress_class,phone_list_pau,
                    phone_before_comma,phone_before_period,phone_before_semicolon,phone_after_comma,phone_after_period,phone_after_semicolon)    
    
    '''

