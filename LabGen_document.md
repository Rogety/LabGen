# LabGen document

## 動機
HTS系統DEMO的合成語音不夠理想，修正其LABEL使的聽起來更流暢和自然


## 實驗流程
1.抓取LABEL的切割時間、PHONENEME、POS 轉成mul檔
- sil和sp取代pau，sil代表句子前後的停頓，sp代表標點符號的停頓，ax替換成ah
- 原本lab所定義的syllable有些問題，所以用我們的字典去切割syllable

2.再從mul檔案產生新的label檔
- 把原本label檔案去蕪存菁，刪除掉一些不必要的因素

3.製作label檔所對應的questionset


## 實驗結果


## 程式
1.label_parsor.py : 舊.lab檔轉成mul檔
2.mul_lab.py : .mul檔轉成新.lab檔

## 執行指令
python ./label_parsor.py
python ./mul_lab.py

## 檔案目錄
> LabGen
>> lab : 存放舊的label
>>> xxx.lab

>> mul : 執行完label_parsor.py後產生，存放.mul檔
>>> xxx.mul

>> output : 執行完mul_lab.py後產生，存放新.lab檔
>>> xxx.lab

>> questions : 修改後的問題集
>>> questions_qst001.hed
>>> questions_utt_qst001.hed
 
>> artic_setnese.txt : 訓練句子整理
>> bu_radio_dict_with_syl.txt : 字典
>> label_parsor.py : 
>> mul_lab.py :
>> 




## phoneme format

total phoneme : 41

|phone |example |translation |
|--- |--- |--- |
|AA	|odd | AA D |
|AE	|at	 | AE T |
|AH	|hut |HH AH T|
|AO	|ought	|AO T|
|AW	|cow	|K AW|
|AY	|hide	|HH AY D|
|B 	|be	|B IY|
|CH	|cheese	|CH IY Z|
|D 	|dee	|D IY|
|DH	|thee	|DH IY|
|EH	|Ed	|EH D|
|ER	|hurt	|HH ER T|
|EY	|ate	|EY T|
|F 	|fee	|F IY|
|G 	|green	|G R IY N|
|HH	|he	|HH IY|
|IH	|it	|IH T|
|IY	|eat	|IY T|
|JH	|gee	|JH IY|
|K 	|key	|K IY|
|L 	|lee	|L IY|
|M 	|me	|M IY|
|N 	|knee	|N IY|
|NG	|ping	|P IH NG|
|OW	|oat	|OW T|
|OY	|toy	|T OY|
|P 	|pee	|P IY|
|R 	|read	|R IY D|
|S 	|sea	|S IY|
|SH	|she	|SH IY|
|T 	|tea	|T IY|
|TH	|theta	|TH EY T AH|
|UH	|hood	|HH UH D|
|UW	|two	|T UW|
|V 	|vee	|V IY|
|W 	|we	|W IY|
|Y 	|yield	|Y IY L D|
|Z 	|zee	|Z IY|
|ZH	|seizure	|S IY ZH ER|
|SIL| | |
|SP| | |

## mul format
mul format : 
start end phone stress word F0 POS F1 P1 F2 P2 

|     |description  |
| --- | --- |
| start | 開始時間 |
| end | 結束時間 |
| phone | 音素 |
| stress | 重音 |
| word | 英文詞 |
| F0 | 詞性是否存在 |
| POS | 何種詞性 |
| F1 | 詞後有無標點符號 |
| P1 | 詞後是甚麼標點符號 |
| F1 | 詞前有無標點符號 |
| P1 | 詞前是甚麼標點符號 |

## label format

p1ˆp2-p3+p4=p5@p6_p7
/A:a1_a2 
/B:b1-b2-b3@b4-b5&b6-b7#b8-b9$b10-b11 
/C:c1+c2
/D:d1_d2 
/E:e1+e2@e3+e4&e5+e6#e7+e8 
/F:f1_f2
/G:g1_g2 
/H:h1=h2ˆh3=h4 
/I:i1_i2
/J:j1+j2-j3

|    | description
| --- | ---
| p1 | the phoneme identity before the previous phoneme
| p2 | the previous phoneme identity
| p3 | the current phoneme identity
| p4 | the next phoneme identity
| p5 | the phoneme after the next phoneme identity
| p6 |position of the current phoneme identity in the current syllable (forward)
| p7 | position of the current phoneme identity in the current syllable (backward)
| a1 | whether the previous syllable stressed or not (0: not stressed, 1: stressed)
| a2 | the number of phonemes in the previous syllable
| b1 | whether the current syllable stressed or not (0: not stressed, 1: stressed)
| b2 | the number of phonemes in the current syllable
| b3 | position of the current syllable in the current word (forward)
| b4 | position of the current syllable in the current word (backward)
| b5 | position of the current syllable in the current phrase (forward)
| b6 | position of the current syllable in the current phrase (backward)
| b7 | the number of stressed syllables before the current syllable in the current phrase
| b8 | the number of stressed syllables after the current syllable in the current phrase
| b9| the number of syllables from the previous stressed syllable to the current syllable
| b10| the number of syllables from the current syllable to the next stressed syllable
| b11| name of the vowel of the current syllable
| c1 | whether the next syllable stressed or not (0: not stressed, 1: stressed)
| c2 | the number of phonemes in the next syllable
| d1 | gpos (guess part-of-speech) of the previous word
| d2 | the number of syllables in the previous word
| e1 | gpos (guess part-of-speech) of the current word
| e2 | the number of syllables in the current word
| e3 | position of the current word in the current phrase (forward)
| e4 | position of the current word in the current phrase (backward)
| e5 | the number of content words before the current word in the current phrase
| e6 | the number of content words after the current word in the current phrase
| e7 | the number of words from the previous content word to the current word
| e8 | the number of words from the current word to the next content word
| f1 | gpos (guess part-of-speech) of the next word
| f2 | the number of syllables in the next word
| g1 | the number of syllables in the previous phrase
| g2 | the number of words in the previous phrase
| h1 | the number of syllables in the current phrase
| h2 | the number of words in the current phrase
| h3 | position of the current phrase in this sentence (forward)
| h4 | position of the current phrase in this sentence (backward)
| i1 | the number of syllables in the next phrase
| i2 | the number of words in the next phrase
| j1 | the number of syllables in this sentence
| j2 | the number of words in this sentence
| j3 | the number of phrases in this sentence

# Question Set

label  | Qestion Set | Description
---    | --- | ---
p1^    | "LL-Vowel\=='ae^'"
^p2-   | "L-Consonant\=='^ch-'"
-p3+   | "C-Fricative\=='-f+'"
+p4=   | "R-EVowel\=='+ey='"
=p5@   | "RR-th\=='=th@'"
@p6_   | "Seg_Fw\==1" 
_p7/A: | "Seg_Bw\==2"
/A:a1_ | "L-Syl_Stress\==0"
_a2/B: | "L-Syl_Num-Segs\==0"
/B:b1- | "C-Syl_Stress\==1"
-b2-   | "C-Syl_Num-Segs\==2"
-b3@   | "Pos_C-Syl_in_C-Word(Fw)\==1"
@b4-   | "Pos_C-Syl_in_C-Word(Bw)\==2"
-b5&   | "Pos_C-Syl_in_C-Phrase(Fw)\==1"
&b6-   |    "Pos_C-Syl_in_C-Phrase(Bw)\==7"
-b7#   |	"Num-StressedSyl_before_C-Syl_in_C-Phrase\==1"
#b8-   |	"Num-StressedSyl_after_C-Syl_in_C-Phrase\==4"
-b9$   |	"Num-Syl_from_prev-StressedSyl\==0"
$b10-  |	"Num-Syl_from_next-StressedSyl\==2" 
-b11/C:|	"vowel"
/C:c1+ |	"R-Syl_Stress\==0"
+c2/D: |	"R-Syl_Num-Segs\==1"
/D:d1_ |    "L-Word_GPOS\==0"
_d2/E: |    "L-Word_Num-Syls\==0"
/E:e1+ |	"C-Word_GPOS\==content"
+e2@   |	"C-Word_Num-Syls\==2"
@e3+   |	"Pos_C-Word_in_C-Phrase(Fw)\==1"
+e4&   |	"Pos_C-Word_in_C-Phrase(Bw)\==5"
&e5+   |	"Num-ContWord_before_C-Word_in_C-Phrase\==1"
+e6#   |	"Num-ContWord_after_C-Word_in_C-Phrase\==2"
#e7+   |	"Num-Words_from_prev-ContWord\==0"
+e8/F: | 	"Num-Words_from_next-ContWord\==3"
/F:f1_ | 	"R-Word_GPOS\==in"
_f2/G: |	"R-Word_Num-Syls\==1"
/G:g1_ |	"L-Phrase_Num-Syls\==0"
_g2/H: |	"L-Phrase_Num-Words\==0"
/H:h1= |	"C-Phrase_Num-Syls\==7"
=h2^   |	"C-Phrase_Num-Words\==5"
^h3=   |	"Pos_C-Phrase_in_Utterance(Fw)\==1"
=h4/I: |	"Pos_C-Phrase_in_Utterance(Bw)\==2"
/I:i1= | 	"R-Phrase_Num-Syls\==7"
=i2/J: | 	"R-Phrase_Num-Words\==3"
/J:j1+ |	"Num-Syls_in_Utterance\==14"
+j2-   |	"Num-Words_in_Utterance\==8"
-j3    |    "Num-Phrases_in_Utterance\==2"                  