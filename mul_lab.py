# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 22:53:02 2019

@author: Aaron
"""

import os

##

def list_shift(listP , direction , count , _type_):
    
    if direction == "right":
        if count == 1:
            listP.pop(-1) ##pop() : 預設是刪掉最後一個
            listP.insert(0 , 'x' )
        elif count == 2: 
            listP.pop(-1)
            listP.pop(-1)
            listP.insert(0 , 'x' )
            listP.insert(0 , 'x' )
    elif direction == "left":
        if count == 1:
            listP.pop(0)
            listP.insert(len(listP) , 'x' )
            ##listP.insert(-1 , 'x' ) 插入在不對的位置 bug??
        elif count == 2: 
            listP.pop(0)
            listP.pop(0)
            listP.insert(len(listP) , 'x' )
            listP.insert(len(listP) , 'x' )
    elif direction == "previous":
        listP.pop() ##pop() : 預設是刪掉最後一個
        if _type_ == "int":
            listP.insert(0 , 0 )
        elif _type_ == "char":
            listP.insert(0 , '0' )
    elif direction == "next":
        listP.pop(0)
        if _type_ == "int":
            listP.insert(len(listP) , 0 )
        elif _type_ == "char":
            listP.insert(len(listP) , '0' )
    else:
        print("arguments error")
        
    #print("listP = ",listP)
    return listP 
    
def Get_text(filepath):
    
    text = []
    with open(filepath , "r+") as f :
        for line in f:
            line = line.split(" ")
            del line[-1]  # 去除"\n"
            text.append(line)
            #print(line)
    
    return text

def Get_word_list(text,syllable_start,word_start,phrase_start,
                  phone_num_in_syllable,phone_num_in_word,phone_num_in_phrase):
    #print("\t\t\tGet_word_list\t\t\t")
    phone_list,syllable_list,word_list,phrase_list = [], [], [], []
    
    ##phone_list
    for i in range(len(text)):
        phone_list.append(text[i][2])
    
    ##syllable_list
    m=0    
    for i in range(len(phone_list)):
        if i == syllable_start[m]:
            n = phone_num_in_syllable[m]
            tmp_syl = ""
            for k in range(0,n):
                tmp_syl += phone_list[i+k]
            syllable_list.append(tmp_syl)
            m=m+1
        if m == len(syllable_start):
            break
    
    ##word_list
    m=0    
    for i in range(len(phone_list)):
        if i == word_start[m]:
            n = phone_num_in_word[m]
            tmp_word = ""
            for k in range(0,n):
                tmp_word += phone_list[i+k]
            word_list.append(tmp_word)
            m=m+1
        if m == len(word_start):
            break
        
    ##phrase_list
    m=0    
    for i in range(len(phone_list)):
        if i == phrase_start[m]:
            n = phone_num_in_phrase[m]
            tmp_phrase = ""
            for k in range(0,n):
                tmp_phrase += phone_list[i+k]
            phrase_list.append(tmp_phrase)
            m=m+1
        if m == len(phrase_start):
            break
    
    #print("phone_list =",phone_list,len(phone_list))         
    #print("syllable_list =",syllable_list,len(syllable_list))
    #print("word_list =",word_list,len(word_list))
    #print("phrase_list =",phrase_list,len(phrase_list))
    
    return phone_list,syllable_list,word_list,phrase_list

def Get_phone_num(text):
    #print("\t\t\tGet_phone_num\t\t\t")
    
    phone_num_in_syllable,phone_num_in_word,phone_num_in_phrase = [],[],[]
    
    text_tmp = []
    for line in text:
        if line[2] != 'sil' and line[2] != 'sp':
            text_tmp.append(line)
            
    syl_start,word_start,phrase_start = [],[],[]
    
    phrase_start.append(0)
    for i in range(len(text_tmp)):  
        if len(text_tmp[i]) > 4:
            word_start.append(i)
        if len(text_tmp[i]) > 3:
            syl_start.append(i)
        if text_tmp[i][-1] == ',':
            phrase_start.append(i)
        
    
            
    # print(word_start,len(word_start))
    # print(syl_start,len(syl_start))    
    # print(phrase_start,len(phrase_start))

    for i in range(len(word_start)):
        try:
            phone_num_in_word.append(word_start[i+1] - word_start[i])
        except IndexError:
            phone_num_in_word.append(len(text_tmp) - word_start[i])
            
    for i in range(len(syl_start)):
        try:
            phone_num_in_syllable.append(syl_start[i+1] - syl_start[i])
        except IndexError:
            phone_num_in_syllable.append(len(text_tmp) - syl_start[i])
    
    for i in range(len(phrase_start)):
        try:
            phone_num_in_phrase.append(phrase_start[i+1] - phrase_start[i])
        except IndexError:
            phone_num_in_phrase.append(len(text_tmp) - phrase_start[i])
            
            
    # print(phone_num_in_word , len(phone_num_in_word))
    # print(phone_num_in_syllable , len(phone_num_in_syllable))
    # print(phone_num_in_phrase , len(phone_num_in_phrase))
            
    return phone_num_in_syllable,phone_num_in_word,phone_num_in_phrase
    

def Get_syllable_num(phone_num_in_syllable,phone_num_in_word,phone_num_in_phrase):
    #print("\t\t\tGet_syllable_num\t\t\t")
    
    syllable_num_in_word,syllable_num_in_phrase,syllable_num_in_utterance =[],[],[]
    
    # print(phone_num_in_word , len(phone_num_in_word))
    # print(phone_num_in_syllable , len(phone_num_in_syllable))
    # print(phone_num_in_phrase , len(phone_num_in_phrase))
    
    ##
    k=0
    for val in phone_num_in_word:
        tmp,count = 0,0
        if val == phone_num_in_syllable[k]:
            syllable_num_in_word.append(1)
            k += 1
        else:
            while( tmp != val ):
                tmp += phone_num_in_syllable[k]
                k += 1
                count += 1
            syllable_num_in_word.append(count)
      
    ##
    k=0
    for val in phone_num_in_phrase:
        tmp,count = 0,0
        if val == phone_num_in_syllable[k]:
            syllable_num_in_phrase.append(1)
            k += 1
        else:
            while( tmp != val ):
                tmp += phone_num_in_syllable[k]
                k += 1
                count += 1
            syllable_num_in_phrase.append(count)
    
    ##        
    syllable_num_in_utterance.append(len(phone_num_in_syllable))
            
    
    # print("syllable_num_in_word = ",syllable_num_in_word,len(syllable_num_in_word))
    # print("syllable_num_in_phrase = ",syllable_num_in_phrase,len(syllable_num_in_phrase))
    # print("syllable_num_in_utterance = ",syllable_num_in_utterance,len(syllable_num_in_utterance))
    
    
    return syllable_num_in_word,syllable_num_in_phrase,syllable_num_in_utterance

def Get_word_num(phone_num_in_word,phone_num_in_phrase):
    
    word_num_in_phrase,word_num_in_utterance = [],[]
    # print(phone_num_in_word)
    # print(phone_num_in_phrase)
    
    k=0
    for val in phone_num_in_phrase:
        tmp,count = 0,0
        if val == phone_num_in_word[k]:
            word_num_in_phrase.append(1)
            k += 1
        else:
            while( tmp != val ):
                tmp += phone_num_in_word[k]
                k += 1
                count += 1
            word_num_in_phrase.append(count)
            
    word_num_in_utterance.append(len(phone_num_in_word))
            
    # print("word_num_in_phrase = ",word_num_in_phrase,len(word_num_in_phrase))
    # print("word_num_in_utterance = ",word_num_in_utterance,len(word_num_in_utterance))            
    
    
    return word_num_in_phrase,word_num_in_utterance

def Get_phrase_num(phone_num_in_phrase):
    
    phrase_num_in_utterance = []
    
    phrase_num_in_utterance.append(len(phone_num_in_phrase))
    
    # print("phrase_num_in_utterance = ",phrase_num_in_utterance,len(phrase_num_in_utterance))  
    
    return phrase_num_in_utterance

def Get_start_stamp(text):
    #print("\t\t\tGet_start_stamp\t\t\t")
    line_count = []
    phone_start = []
    syllable_start,word_start,phrase_start = [],[],[]
    sentence_start = [1]
    
    for line in text :
        line_count.append(len(line))
        
        #print(line)
        
    #print(line_count , len(line_count))
    
    for i in range(len(text)):
        if text[i][2] != 'sil' and text[i][2] != 'sp':
            phone_start.append(i)
    
    for i in range(len(line_count)):
        if line_count[i] > 4 :
            word_start.append(i)
        if line_count[i] > 3 :
            syllable_start.append(i)
        
    phrase_start.append(1)
    for i in range(len(text)):
        if text[i][-1] == ',':
            phrase_start.append(i)
    
    #print(phone_start , len(phone_start))
    
    return phone_start,syllable_start ,word_start , phrase_start,sentence_start


def Get_time(text):
    
    #print("\t\t\tGet_time\t\t\t")
    start , end = [] , []
    
    for line in text :
        start.append(line[0])
        end.append(line[1])
    

    
    return start , end

def Get_stress_info(text):
    #print("\t\t\tGet_stress_info\t\t\t")
    stress_index,stress_type = [],[]
    
    ##stress_index =sylstart
    
    for line in text :
        try :
            if line[3] == '2':  ## 
                stress_type.append('1')
            else:
                stress_type.append(line[3])
        except :
            pass
    
    return stress_index,stress_type

def Get_GPOS_info(text):
    #print("\t\t\tGet_GPOS_info\t\t\t")
    GPOS_list = []
    
    for line in text:
        if len(line) > 6:
            GPOS_list.append(line[6])
    
    return GPOS_list

def Generate_single_label(text,target_list,syllable_start,word_start,phrase_start,sentence_start, _type_):
    
    label = []
    k=0
    if _type_ == "int":
        val = 0
    elif _type_ == "char":
        val = '0'
    
    if syllable_start != [] and word_start == [] and phrase_start == [] :
        for i in range(len(text)):
            if i == syllable_start[k]:
                val = target_list[k]
                k += 1
                if k == len(syllable_start):
                    k = len(syllable_start)-1
               
            if text[i][2] == 'sp' or text[i][2] == 'sil':
                label.append('x')
            else:
                label.append(val) 
    
    if word_start != [] and syllable_start == [] and phrase_start == []:
        for i in range(len(text)):
            if i == word_start[k]:
                val = target_list[k]
                k += 1
                if k == len(word_start):
                    k = len(word_start)-1
               
            if text[i][2] == 'sp' or text[i][2] == 'sil':
                label.append('x')
            else:
                label.append(val) 
                
    if phrase_start != [] and syllable_start == [] and word_start == []:
        for i in range(len(text)):
            if i == phrase_start[k]:
                val = target_list[k]
                k += 1
                if k == len(phrase_start):
                    k = len(phrase_start)-1
               
            if text[i][2] == 'sp' or text[i][2] == 'sil':
                label.append('x')
            else:
                label.append(val) 
    
    if sentence_start:
        for i in range(len(text)):
            if i == sentence_start[k]:
                val = target_list[k]
                k += 1
                if k == len(sentence_start):
                    k = len(sentence_start)-1
               
            if text[i][2] == 'sp' or text[i][2] == 'sil':
                label.append('x')
            else:
                label.append(val) 

            
    return label

def Generate_position_label(target_list,start_short,strat_long):
    
    label_forward,label_backward = [],[]
    
    k = 0
    m = 0
    forward = 0
    backward = 0
    for i in range(len(text)):
        if i == strat_long[k]:
            forward = 0 
            backward = target_list[k]+1 ## not good expression
            k += 1
            if k == len(strat_long):
                k = len(strat_long)-1
                    
        if i == start_short[m]:
            forward += 1
            backward -= 1
            m += 1
            if m == len(start_short):
                m = len(start_short)-1
    
        if text[i][2] == 'sp' or text[i][2] == 'sil':
            label_forward.append('x')
            label_backward.append('x')
        else:
            label_forward.append(forward)
            label_backward.append(backward)
    
    return label_forward , label_backward

def Get_P_lab(text,phone_start,syllable_start,phone_num_in_syllable,phone_list):
    
    #print("\t\t\tGet_P_lab\t\t\t")
    P1,P2,P3,P4,P5,P6,P7 = [],[],[],[],[],[],[]
    
    for line in text :
        if line[2] == 'sil':
            P3.append('sil')
        elif line[2] == 'sp':
            P3.append('sp')
        else :
            P3.append(line[2].lower())
        
    P1 = list_shift(P3.copy() , "right" , 2 , _)
    P2 = list_shift(P3.copy() , "right" , 1 , _)
    P4 = list_shift(P3.copy() , "left" , 1 , _)
    P5 = list_shift(P3.copy() , "left" , 2 , _)
    P6,P7 = Generate_position_label(phone_num_in_syllable,phone_start,syllable_start)   
       
    return P1 , P2 , P3 , P4 , P5 , P6 , P7
    
def Get_A_lab(text,phone_start,syllable_start,phone_num_in_syllable,stress_type):
    
    A1,A2 =[],[]
    stress_type_in_previous_syllable,phone_num_in_previous_syllable = [],[]
    #print("\t\t\tGet_A_lab\t\t\t")
    
    phone_num_in_previous_syllable = list_shift(phone_num_in_syllable.copy(),"previous", _ , "int")    
    stress_type_in_previous_syllable = list_shift(stress_type.copy(),"previous", _ , "char")
   
    A1 = Generate_single_label(text,stress_type_in_previous_syllable,syllable_start,_,_,_, "int")
    A2 = Generate_single_label(text,phone_num_in_previous_syllable,syllable_start,_,_,_, "int")

    return A1,A2

def xxx_num_before_curent_xxx_in_phrase(text,target_list,start_short,start_long):
    
    label = []
    k,m,count=0,0,0
    for i in range(len(text)):                
        if i == start_short[k]:
            count += int(target_list[k])
            k += 1
            if k == len(start_short):
                k = len(start_short)-1
        
        if i == start_long[m]:  ## phrase中在第一個syllable 一定是0個 stressed syllable 
            count = 0
            m += 1
            if m == len(start_long):
                m = len(start_long)-1
        
        if text[i][2] == 'sil' or text[i][2] == 'sp':
            label.append('x')
        else :
            label.append(count)
    
    
    return label

def xxx_num_after_curent_xxx_in_phrase(text,target_list_short,target_list_long,start_short,start_long):
    
    label = []
    k,m,count=0,0,0
    for i in range(len(text)):
        if i == start_long[m]:
            count = target_list_long[m]
            m += 1
            if m == len(start_long):
                m = len(start_long)-1
                
        if i == start_short[k]:
            count -= int(target_list_short[k])
            k += 1
            if k == len(start_short):
                k = len(start_short)-1
        
        if text[i][2] == 'sil' or text[i][2] == 'sp':
            label.append('x')
        else :
            label.append(count)
    
    return label

def xxx_num_from_previous_xxx_to_current_xxx(text,target_list_short,target_list_long,start_short,start_long):
    label = []
    
    count,k=0,0
    for i in range(len(text)):                               
        if i == start_short[k]:
            n = k -1 ## m = index
            count = 0
            
            try:
                while target_list_short[n] != '1' : 
                    n = n + 1
                    count += 1
            except :
                pass
            
            k += 1
            if k == len(start_short):
                k = len(start_short)-1
        if text[i][2] == 'sil' or text[i][2] == 'sp':
            label.append('x')
        else :
            label.append(count)
    
    return label

def xxx_num_from_current_xxx_to_next_xxx(text,target_list_short,target_list_long,start_short,start_long):
    label = []
    
    count,k=0,0
    for i in range(len(text)):               
        if i == start_short[k]:
            n = k + 1 ## N = index
            count = 0
            if n == len(target_list_short):
                n = len(target_list_short) - 1
            try :
                while target_list_short[n] != '1' : 
                    n = n + 1
                    count += 1
            except :
                pass

            k += 1
            if k == len(start_short):
                k = len(start_short)-1
                
        if text[i][2] == 'sil' or text[i][2] == 'sp':
            label.append('x')
        else :
            label.append(count)
    return label

def Get_B_lab(
            text,phone_start,syllable_start,word_start,phrase_start,
            phone_num_in_syllable,syllable_num_in_word,syllable_num_in_phrase,
            stress_type):
    
    #print("\t\t\tGet_B_lab\t\t\t")
    B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11 = [],[],[],[],[],[],[],[],[],[],[]
    
    stress_type_in_current_syllable = stress_type.copy()
    phone_num_in_current_syllable = phone_num_in_syllable.copy()
    current_syllable_num_in_current_word = syllable_num_in_word.copy()
    current_syllable_num_in_current_phrase = syllable_num_in_phrase.copy()
#    print("phone_num_in_current_syllable =",phone_num_in_current_syllable ,len(phone_num_in_current_syllable))
#    print("stress_type_in_current_syllable =",stress_type_in_current_syllable ,len(stress_type_in_current_syllable))
#    print("current_syllable_num_in_current_phrase =",current_syllable_num_in_current_phrase ,len(current_syllable_num_in_current_phrase))
#    print("syllable_num_in_word =",syllable_num_in_word,len(syllable_num_in_word))
#    print("word_start",word_start,len(word_start))
    
    #B7
    total=0
    stressed_num_in_phrase = []
    for val in current_syllable_num_in_current_phrase:
        count=0
        for i in range(total,total+val):
            count += int(stress_type[i])
        total += val
        stressed_num_in_phrase.append(count)
    
    #B9
    phrase_num = len(phrase_start)
    current_syllable_sum_in_current_phrase = []
    sum = 0
    for i in range(0,phrase_num):
        sum += current_syllable_num_in_current_phrase[i]
        current_syllable_sum_in_current_phrase.append(sum)
    current_syllable_sum_in_current_phrase.insert(0,0)
#    print(current_syllable_sum_in_current_phrase)
#    print("stressed_num_in_phrase =",stressed_num_in_phrase)    
    # B11
    syl_vowel = [] 
    vowel_list = ['AA','AE','AH','AO','AY','AW','EH','ER','EY','IH','IY','OY','UW','UH','OW','novowel'] 
    ##  "S" , "Z" 為了所有格的BUG
    for line in text:

        if line[2] in vowel_list:
            syl_vowel.append(line[2])   
        
        if len(line) > 4:
            if line[4] == "'s":  ##  for 's case
                syl_vowel.append('novowel')

        
    #print(syl_vowel , len(syl_vowel) , len(syllable_start))   
    if len(syl_vowel) != len(syllable_start):
        print("vowl_list_not_enough")
    
    B1 = Generate_single_label(text,stress_type_in_current_syllable,syllable_start,_,_,_, "int")
    B2 = Generate_single_label(text,phone_num_in_current_syllable,syllable_start,_,_,_, "int")     
    B3,B4 = Generate_position_label(current_syllable_num_in_current_word,syllable_start,word_start)
    B5,B6 = Generate_position_label(current_syllable_num_in_current_phrase,syllable_start,phrase_start)   
    stress_type_shift_right = list_shift(stress_type.copy(),"previous", _ , "int" )    
    B7 = xxx_num_before_curent_xxx_in_phrase(text,stress_type_shift_right,syllable_start,phrase_start)
    B8 = xxx_num_after_curent_xxx_in_phrase(text,stress_type,stressed_num_in_phrase,syllable_start,phrase_start)                
    B9 = xxx_num_from_previous_xxx_to_current_xxx(text,stress_type,current_syllable_sum_in_current_phrase,syllable_start,phrase_start)
    B10 =xxx_num_from_current_xxx_to_next_xxx(text,stress_type,current_syllable_sum_in_current_phrase,syllable_start,phrase_start)    
    B11 = Generate_single_label(text,syl_vowel,syllable_start,_,_,_, "int")
    
#    print("B1 =",B1,len(B1))
#    print("B2 =",B2,len(B2))
#    print("B3 =",B3,len(B3))
#    print("B4 =",B4,len(B4))
#    print("current_syllable_num_in_current_phrase =",current_syllable_num_in_current_phrase,
#          len(current_syllable_num_in_current_phrase))
#    print("B5 =",B5,len(B5))
#    print("B6 =",B6,len(B6))
#    print("stress_type_in_current_syllable =",stress_type_in_current_syllable ,len(stress_type_in_current_syllable))
#    print("current_syllable_num_in_current_phrase =",current_syllable_num_in_current_phrase ,len(current_syllable_num_in_current_phrase))
#    print("B7 =",B7,len(B7))
#    print("B8 =",B8,len(B8))
#    print("B9 =",B9,len(B9))
#    print("B10 =",B10,len(B10))
     # print("B11 =",B11,len(B11))
    
    return B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11


def Get_C_lab(text,syllable_start,phone_num_in_syllable,stress_type):
    #print("\t\t\tGet_C_lab\t\t\t")
    
    phone_num_in_next_syllable = list_shift(phone_num_in_syllable.copy(),"next", _ , "int")
    stress_type_in_next_syllable = list_shift(stress_type.copy(),"next", _ , "char" )
            
    C1 = Generate_single_label(text,stress_type_in_next_syllable,syllable_start,_,_,_, "int")
    C2 = Generate_single_label(text,phone_num_in_next_syllable,syllable_start,_,_,_, "int")
    
    return C1 , C2 


    

def Get_D_lab(text,word_start,syllable_num_in_word,GPOS_list):
    #print("\t\t\tGet_D_lab\t\t\t")
   
    GPOS_list_in_previous_word = list_shift(GPOS_list.copy(),"previous", _ , "char")
    syllable_num_in_previous_word = list_shift(syllable_num_in_word.copy(),"previous", _ , "int" )
#    print(syllable_num_in_word)
#    print(syllable_num_in_previous_word)
    D1 = Generate_single_label(text, GPOS_list_in_previous_word,_ ,word_start, _ , _,"char")    
    D2 = Generate_single_label(text, syllable_num_in_previous_word,_ ,word_start, _ ,_, "int")
    
#    print("D1 =",D1,len(D1))
#    print("D2 =",D2,len(D2))
    return D1,D2 



def Get_E_lab(text,word_start,phrase_start,
            syllable_num_in_word,word_num_in_phrase,GPOS_list):
    #print("\t\t\tGet_E_lab\t\t\t")
    
    E1,E2,E3,E4,E5,E6,E7,E8 = [],[],[],[],[],[],[],[]
    
    GPOS_list_in_current_word = GPOS_list.copy()
    syllable_num_in_current_word = syllable_num_in_word.copy()
    word_num_in_current_phrase = word_num_in_phrase.copy()

    ##E5,E6,E7,E8
#    print(GPOS_list)
    content_index = []  ## ==len(word)
    for item in GPOS_list:
        if item == 'content':
            content_index.append('1')
        else:
            content_index.append('0')
#    print("content_index =",content_index,len(content_index))
    
    content_word_num_in_phrase = []
#    print("word_num_in_phrase =",word_num_in_phrase,len(word_num_in_phrase))
   
    total=0
    for val in word_num_in_phrase:
        count=0
        for i in range(total,total+val):
            count += int(content_index[i])
        total += val
        content_word_num_in_phrase.append(count)
#    print("content_word_num_in_phrase =",content_word_num_in_phrase) 
    
    content_index_shift_right = list_shift(content_index.copy(),"previous", _ , "char" )
#    print("content_index =",content_index,len(content_index))
       
    phrase_num = len(phrase_start)
    current_word_sum_in_current_phrase = []
    sum = 0
    for i in range(0,phrase_num):
        sum += word_num_in_current_phrase[i]
        current_word_sum_in_current_phrase.append(sum)
    current_word_sum_in_current_phrase.insert(0,0)
#    print(current_word_sum_in_current_phrase)

    
    E1 = Generate_single_label(text, GPOS_list_in_current_word , _, word_start, _,_, "char")
    E2 = Generate_single_label(text, syllable_num_in_current_word,_ , word_start, _,_, "int")            
    E3,E4 = Generate_position_label(word_num_in_current_phrase,word_start,phrase_start)
    E5 = xxx_num_before_curent_xxx_in_phrase(text,content_index_shift_right,word_start,phrase_start)
    E6 = xxx_num_after_curent_xxx_in_phrase(text,content_index,content_word_num_in_phrase,word_start,phrase_start)    
    E7 = xxx_num_from_previous_xxx_to_current_xxx(text,content_index,current_word_sum_in_current_phrase,word_start,phrase_start)
    E8 =xxx_num_from_current_xxx_to_next_xxx(text,content_index,current_word_sum_in_current_phrase,word_start,phrase_start)
    

    
    return E1,E2,E3,E4,E5,E6,E7,E8 

def Get_F_lab (text,word_start,syllable_num_in_word,GPOS_list):
    #print("\t\t\tGet_F_lab\t\t\t")
    F1,F2 =[],[]
    
    GPOS_list_in_next_word = list_shift(GPOS_list.copy(),"next", _ , "char")
    syllable_num_in_next_word = list_shift(syllable_num_in_word.copy(),"next", _ , "int" )
#    print(syllable_num_in_word)
#    print(syllable_num_in_next_word)
    F1 = Generate_single_label(text, GPOS_list_in_next_word,_ ,word_start, _ ,_, "char")    
    F2 = Generate_single_label(text, syllable_num_in_next_word, _ ,word_start, _ ,_, "int")
    
#    print("F1 =",F1,len(F1))
#    print("F2 =",F2,len(F2))
      
    return F1 , F2 

def Get_G_lab(text,phrase_start,syllable_num_in_phrase,word_num_in_phrase):
    #print("\t\t\tGet_G_lab\t\t\t")
    G1,G2 = [],[]
    
    syllable_num_in_previous_phrase = list_shift(syllable_num_in_phrase.copy(),"previous",_,"int")
    word_num_in_previous_phrase = list_shift(word_num_in_phrase.copy() , "previous",_,"int" )
#    print(syllable_num_in_phrase)
#    print(syllable_num_in_previous_phrase)
#    print(word_num_in_phrase)
#    print(word_num_in_previous_phrase)
    G1 = Generate_single_label(text, syllable_num_in_previous_phrase, _ ,_, phrase_start,_, "int")
    G2 = Generate_single_label(text, word_num_in_previous_phrase, _ ,_, phrase_start ,_, "int")
    
#    print("G1 =",G1,len(G1))
#    print("G2 =",G2,len(G2))
    
    
    return G1,G2 

def Get_H_lab(text,phrase_start,sentence_start,syllable_num_in_phrase,word_num_in_phrase,phrase_num_in_sentence):
    #print("\t\t\tGet_H_lab\t\t\t")
    H1,H2,H3,H4 = [],[],[],[]
    
    syllable_num_in_current_phrase = syllable_num_in_phrase.copy()
    word_num_in_current_phrase = word_num_in_phrase.copy()
    
    H1 = Generate_single_label(text, syllable_num_in_current_phrase, _ ,_, phrase_start,_, "int")
    H2 = Generate_single_label(text, word_num_in_current_phrase, _ ,_, phrase_start ,_, "int")
    
#    print("H1 =",H1,len(H1))
#    print("H2 =",H2,len(H2))        
    
    #H3 H4
    H3,H4 = Generate_position_label(phrase_num_in_sentence,phrase_start,sentence_start)
    
#    print("H3 =",H3,len(H3))
#    print("H4 =",H4,len(H4))
    
    return H1,H2,H3,H4

def Get_I_lab(text,phrase_start,syllable_num_in_phrase,word_num_in_phrase):
    #print("\t\t\tGet_I_lab\t\t\t")
    
    syllable_num_in_next_phrase = list_shift(syllable_num_in_phrase.copy(),"next",_,"int")
    word_num_in_next_phrase = list_shift(word_num_in_phrase.copy() , "next",_,"int" )
    
    I1 = Generate_single_label(text, syllable_num_in_next_phrase,_ ,_, phrase_start,_, "int")
    I2 = Generate_single_label(text, word_num_in_next_phrase, _ ,_, phrase_start ,_, "int")
    
#    print("I1 =",I1,len(I1))
#    print("I2 =",I2,len(I2))
    
    return I1,I2 

def Get_J_lab(text,sentence_start,syllable_num_in_sentence,word_num_in_sentence,phrase_num_in_sentence):
    #print("\t\t\tGet_J_lab\t\t\t")
    J1,J2,J3 =[],[],[]
    
    J1 = Generate_single_label(text, syllable_num_in_sentence,_ ,_, _,sentence_start, "int")
    J2 = Generate_single_label(text, word_num_in_sentence,_ ,_, _ ,sentence_start, "int")
    J3 = Generate_single_label(text, phrase_num_in_sentence,_ ,_, _,sentence_start, "int")

#    print("J1 =",J1,len(J1))
#    print("J2 =",J2,len(J2))
#    print("J3 =",J3,len(J3))
    
    return J1,J2,J3


def Generate_lab_out(filepath,text,Start,End,P1,P2,P3,P4,P5,P6,P7,A1,A2,
                     B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,
                     C1,C2,D1,D2,E1,E2,E3,E4,E5,E6,E7,E8,
                     F1,F2,G1,G2,H1,H2,H3,H4,I1,I2,J1,J2,J3):
    
    filepath = filepath.rstrip(".mul")  
    filepath = filepath.lstrip("./mul/")
    filepath1 = "./output/full/" + filepath + ".lab"
    filepath2 = "./output/mono/" + filepath + ".lab"
    
    folder = os.path.exists("./output/")
    if not folder:
        os.makedirs("./output/full/")
        os.makedirs("./output/mono/")
    
    with open(filepath1 , "w+") as f :
        for i in range(len(text)):
            time = "{:>8}".format(Start[i]) +"  " + "{:>8}".format(End[i] + " ")
            P_lab = P1[i]+"^"+P2[i]+"-"+P3[i]+"+"+P4[i]+"="+P5[i]+"@"+str(P6[i])+"_"+str(P7[i])
            A_lab = "/A:"+str(A1[i])+"_"+str(A2[i])
            B_lab = "/B:"+str(B1[i])+"-"+str(B2[i])+"-"+str(B3[i])+"@"+str(B4[i])+"-"+str(B5[i])+"&"+ \
                    str(B6[i])+"-"+str(B7[i])+"#"+str(B8[i])+"-"+str(B9[i])+"$"+str(B10[i])+"-"+B11[i]
            C_lab = "/C:"+C1[i]+"+"+str(C2[i])
            D_lab = "/D:"+D1[i]+"_"+str(D2[i])
            E_lab = "/E:"+E1[i]+"+"+str(E2[i])+"@"+str(E3[i])+"+"+str(E4[i])+"&"+str(E5[i])+"+"+  \
                    str(E6[i])+"#"+str(E7[i])+"+"+str(E8[i])
            F_lab = "/F:"+F1[i]+"_"+str(F2[i])
            G_lab = "/G:"+str(G1[i])+"_"+str(G2[i])
            H_lab = "/H:"+str(H1[i])+"="+str(H2[i])+"^"+str(H3[i])+"="+str(H4[i])
            I_lab = "/I:"+str(I1[i])+"_"+str(I2[i])
            J_lab = "/J:"+str(J1[i])+"+"+str(J2[i])+"-"+str(J3[i])
            
            
            string = time+P_lab+A_lab+B_lab+C_lab+D_lab+E_lab+F_lab+G_lab+H_lab+I_lab+J_lab
            
            f.write(string)
            f.write("\n")
            
    with open(filepath2 , "w+") as f :
        for i in range(len(text)):
            time = "{:>8}".format(Start[i]) +"  " + "{:>8}".format(End[i] + " ")
            phone = ' ' + P3[i]
            
            string = time + phone  

            f.write(string)
            f.write("\n")            
    
    
    return []

if __name__ == '__main__':
    


    '''
    filename = "cmu_us_arctic_slt_a0034.mul"
    print(filename)
    filepath = "./mul/" + filename
    text = Get_text(filepath)    
        
    phone_start,syllable_start,word_start,phrase_start,sentence_start  = Get_start_stamp(text)       
    phone_num_in_syllable,phone_num_in_word,phone_num_in_phrase = Get_phone_num(text)    
    syllable_num_in_word,syllable_num_in_phrase,syllable_num_in_sentence = Get_syllable_num(
            phone_num_in_syllable,phone_num_in_word,phone_num_in_phrase)       
    word_num_in_phrase,word_num_in_sentence = Get_word_num(
            phone_num_in_word,phone_num_in_phrase)           
    phrase_num_in_sentence = Get_phrase_num(phone_num_in_phrase)    
    phone_list,syllable_list,word_list,phrase_list = Get_word_list(
            text,syllable_start,word_start,phrase_start,
            phone_num_in_syllable,phone_num_in_word,phone_num_in_phrase)    
    _ ,stress_type = Get_stress_info(text)        
    GPOS_list = Get_GPOS_info(text)   
    Start , End = Get_time(text)
        
    P1,P2,P3,P4,P5,P6,P7 = Get_P_lab(text,phone_start,syllable_start,phone_num_in_syllable,phone_list)
    A1,A2 = Get_A_lab(text,phone_start,syllable_start,phone_num_in_syllable,stress_type)        
    B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11 = Get_B_lab(
                text,phone_start,syllable_start,word_start,phrase_start,
                phone_num_in_syllable,syllable_num_in_word,syllable_num_in_phrase,
                stress_type)                
    C1,C2 = Get_C_lab(text,syllable_start,phone_num_in_syllable,stress_type)            
    D1,D2 = Get_D_lab(text,word_start,syllable_num_in_word,GPOS_list)       
    E1,E2,E3,E4,E5,E6,E7,E8 = Get_E_lab(
                text,word_start,phrase_start,
                syllable_num_in_word,word_num_in_phrase,
                GPOS_list)           
    F1,F2 = Get_F_lab(text,word_start,syllable_num_in_word,GPOS_list)        
    G1,G2 = Get_G_lab(text,phrase_start,syllable_num_in_phrase,word_num_in_phrase)       
    H1,H2,H3,H4 = Get_H_lab(text,phrase_start,sentence_start,
                                syllable_num_in_phrase,word_num_in_phrase,phrase_num_in_sentence)       
    I1,I2 = Get_I_lab(text,phrase_start,syllable_num_in_phrase,word_num_in_phrase)       
    J1,J2,J3 = Get_J_lab(text,sentence_start,
                             syllable_num_in_sentence,word_num_in_sentence,phrase_num_in_sentence)
    
    Generate_lab_out(filepath,text,Start,End,P1,P2,P3,P4,P5,P6,P7,A1,A2,
                         B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,
                         C1,C2,D1,D2,E1,E2,E3,E4,E5,E6,E7,E8,
                         F1,F2,G1,G2,H1,H2,H3,H4,I1,I2,J1,J2,J3)
    
    print(len(syllable_start),len(stress_type))
    '''
    
    for dirPath, dirNames, fileNames in os.walk("./mul"):
        arctic_fileName = fileNames

    arctic_fileName = arctic_fileName[:]



    for filename in arctic_fileName:
        print("Converting to " + filename)
        filepath = "./mul/" + filename
        text = Get_text(filepath)    
        
        phone_start,syllable_start,word_start,phrase_start,sentence_start  = Get_start_stamp(text)       
        phone_num_in_syllable,phone_num_in_word,phone_num_in_phrase = Get_phone_num(text)    
        syllable_num_in_word,syllable_num_in_phrase,syllable_num_in_sentence = Get_syllable_num(
            phone_num_in_syllable,phone_num_in_word,phone_num_in_phrase)       
        word_num_in_phrase,word_num_in_sentence = Get_word_num(
            phone_num_in_word,phone_num_in_phrase)           
        phrase_num_in_sentence = Get_phrase_num(phone_num_in_phrase)    
        phone_list,syllable_list,word_list,phrase_list = Get_word_list(
            text,syllable_start,word_start,phrase_start,
            phone_num_in_syllable,phone_num_in_word,phone_num_in_phrase)    
        _ ,stress_type = Get_stress_info(text)        
        GPOS_list = Get_GPOS_info(text)   
        Start , End = Get_time(text)
        
        P1,P2,P3,P4,P5,P6,P7 = Get_P_lab(text,phone_start,syllable_start,phone_num_in_syllable,phone_list)
        A1,A2 = Get_A_lab(text,phone_start,syllable_start,phone_num_in_syllable,stress_type)        
        B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11 = Get_B_lab(
                text,phone_start,syllable_start,word_start,phrase_start,
                phone_num_in_syllable,syllable_num_in_word,syllable_num_in_phrase,
                stress_type)                
        C1,C2 = Get_C_lab(text,syllable_start,phone_num_in_syllable,stress_type)            
        D1,D2 = Get_D_lab(text,word_start,syllable_num_in_word,GPOS_list)       
        E1,E2,E3,E4,E5,E6,E7,E8 = Get_E_lab(
                text,word_start,phrase_start,
                syllable_num_in_word,word_num_in_phrase,
                GPOS_list)           
        F1,F2 = Get_F_lab(text,word_start,syllable_num_in_word,GPOS_list)        
        G1,G2 = Get_G_lab(text,phrase_start,syllable_num_in_phrase,word_num_in_phrase)       
        H1,H2,H3,H4 = Get_H_lab(text,phrase_start,sentence_start,
                                syllable_num_in_phrase,word_num_in_phrase,phrase_num_in_sentence)       
        I1,I2 = Get_I_lab(text,phrase_start,syllable_num_in_phrase,word_num_in_phrase)       
        J1,J2,J3 = Get_J_lab(text,sentence_start,
                             syllable_num_in_sentence,word_num_in_sentence,phrase_num_in_sentence)
    
        Generate_lab_out(filepath,text,Start,End,P1,P2,P3,P4,P5,P6,P7,A1,A2,
                         B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,
                         C1,C2,D1,D2,E1,E2,E3,E4,E5,E6,E7,E8,
                         F1,F2,G1,G2,H1,H2,H3,H4,I1,I2,J1,J2,J3)
        
  
