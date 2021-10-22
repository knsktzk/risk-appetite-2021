import streamlit as st
from PIL import Image
import random
import numpy as np
import time

# 箱D
def box_D(Q_num):
    
    dic = {
      
    # question 4
    22: 0, 23: 5, 24: 10, 25: 15, 26: 20, 27: 25, 28: 30, 29: 35, 30: 40, 31: 45, 32: 50, 33: 55, 34: 60, 35: 65, 36: 70, 37: 75, 38: 80, 39: 85, 40: 90, 41: 95, 42: 100,

    # question 5
    43: 100, 44: 95, 45: 90, 46: 85, 47: 80, 48: 75, 49: 70, 50: 65, 51: 60, 52: 55, 53: 50, 54: 45, 55: 40, 56: 35, 57: 30, 58: 25, 59: 20, 60: 15, 61: 10, 62: 5, 63: 0,

    # question 6
    64: 0, 65: 5, 66: 10, 67: 15, 68: 20, 69: 25, 70: 30, 71: 35, 72: 40, 73: 45, 74: 50, 75: 55, 76: 60, 77: 65, 78: 70, 79: 75, 80: 80, 81: 85, 82: 90, 83: 95, 84: 100,

    # question 7
    85: 100, 86: 95, 87: 90, 88: 85, 89: 80, 90: 75, 91: 70, 92: 65, 93: 60, 94: 55, 95: 50, 96: 45, 97: 40, 98: 35, 99: 30, 100: 25, 101: 20, 102: 15, 103: 10, 104: 5, 105: 0,

    # question 8
    106: 0, 107: 5, 108: 10, 109: 15, 110: 20, 111: 25, 112: 30, 113: 35, 114: 40, 115: 45, 116: 50, 117: 55, 118: 60, 119: 65, 120: 70, 121: 75, 122: 80, 123: 85, 124: 90, 125: 95, 126: 100, 

    # question 9
    127: 100, 128: 95, 129: 90, 130: 85, 131: 80, 132: 75, 133: 70, 134: 65, 135: 60, 136: 55, 137: 50, 138: 45, 139: 40, 140: 35, 141: 30, 142: 25, 143: 20, 144: 15, 145: 10, 146: 5, 147: 0,
    
    }
    
    # ball num
    red = dic[Q_num]
    blue = 100 - red
    
    # return
    output_text = "箱Dには赤の玉が {red} 個，青の玉が {blue} 個入っています．".format( red = red, blue = blue)
    st.write( output_text )

# 質問1~3
def question_AB(Q_num, Q_data, dic):
    
    # stock value
    stock_A = 10
    stock_B_red = Q_data[0]
    stock_B_blue = Q_data[1]
    num = 200
    
    #output text
    a_red = num * stock_B_red
    a_blue = num * stock_B_blue
    i = dic[Q_num] * stock_A
    
    st.write("{Q_num} が選ばれました．".format(Q_num = Q_num))
    st.write("【あなたの回答が  {left_choice} の場合】".format(left_choice = Q_data[3]))
    st.write("箱B{box_num}から玉を一つ取り出します．".format(box_num = Q_data[2]))
    st.write("赤が出た場合，謝礼金は {a_red} 円です.".format(a_red = a_red))
    st.write("青が出た場合，謝礼金は {a_blue} 円です.".format(a_blue = a_blue))
    st.write("【あなたの回答が  {right_choice} の場合】".format(right_choice = Q_data[4]))
    st.write("謝礼金は {i} 円です.".format(i = i,))

# 質問4~9
def question_CD(Q_num, Q_data):
    
    # stock value
    num = 200
    C_red = Q_data[0] * num
    C_blue = Q_data[1] * num
    D_red = Q_data[2] * num
    D_blue = Q_data[3] * num
    
    #output text
    st.write("{Q_num} が選ばれました．".format(Q_num = Q_num))
    st.write("【あなたの回答が  {left_choice} の場合】".format(left_choice = Q_data[5]))
    st.write("箱C{box_num}から玉を一つ取り出します．".format(box_num = Q_data[4],))
    st.write("赤が出た場合，謝礼金は {C_red} 円です.".format(C_red = C_red))
    st.write("青が出た場合，謝礼金は {C_blue} 円です.".format(C_blue = C_blue))
    st.write("{left_choice} を選択していた場合，リンク先へ進んでください．https://share.streamlit.io/kt0zuka/dice/main.py".format(left_choice = Q_data[5]))
    st.write("")
    st.write("【あなたの回答が  {right_choice} の場合】".format(right_choice = Q_data[6]))
    st.write("箱Dから玉を一つ取り出します．")
    box_D(Q_num)
    st.write("赤が出た場合，謝礼金は {D_red} 円です.".format(D_red = D_red))
    st.write("青が出た場合，謝礼金は {D_blue} 円です.".format(D_blue = D_blue))

# select your question number for reward money
def select():
    
    # select your question number for reward money
    selected_q = random.randint(1, 147)
    return selected_q

# 質問1~3の分岐
def process_AB(Q_num):
    
    # question(1-3) data = [B_red, B_blue, box number, left choice, right choice]
    q01_data = [12, 9, 1, "ア", "イ"] 
    q02_data = [13, 8, 2, "ウ", "エ"] 
    q03_data = [14, 7, 3, "オ", "カ"] 

    # Dictionary of number of stocks
    q01_dic = {1:175, 2:185, 3:195, 4:205, 5:215}
    q02_dic = {6:155, 7:165, 8:175, 9:185, 10:195, 11:205, 12:215, }
    q03_dic = {13: 135,14: 145,15: 155,16: 165,17: 175,18: 185,19: 195,20: 205,21: 215,}
    
    if 1 <= Q_num <= 5: #question 1
        question_AB(Q_num, q01_data, q01_dic)

    elif 6 <= Q_num <= 12: #question 2
        question_AB(Q_num, q02_data, q02_dic)

    elif 13 <= Q_num <= 21: #question 3
        question_AB(Q_num, q03_data, q03_dic)

# 質問4~9の分岐
def process_CD(Q_num):
    
    # question(4-9) data = [C_red, C_blue, D_red, D_blue, box number, left choice, right choice]
    q04_data = [12, 9, 12, 9, 1, "キ", "ク"]
    q05_data = [  9, 12, 9, 12, 1, "ケ", "コ"]
    q06_data = [13, 8, 13, 8, 2, "サ", "シ"]
    q07_data = [  8, 13, 8, 13, 2, "ス", "セ"]
    q08_data = [14, 7, 14, 7, 3, "ソ", "タ"]
    q09_data = [  7, 14, 7, 14, 3, "チ", "ツ"]
    
    if 22 <= Q_num <= 42: #question 4
        question_CD(Q_num, q04_data)

    elif 43 <= Q_num <= 63: #question 5
        question_CD(Q_num, q05_data)

    elif 64 <= Q_num <= 84: #question 6
        question_CD(Q_num, q06_data)

    elif 85 <= Q_num <= 105: #question 7
        question_CD(Q_num, q07_data)

    elif 106 <= Q_num <= 126: #question 8
        question_CD(Q_num, q08_data)

    elif 127 <= Q_num <= 147: #question 9
        question_CD(Q_num, q09_data)

# main
def main(Q_num):

    if Q_num < 22:
        process_AB(Q_num)
        
    elif 22<= Q_num < 148:
        process_CD(Q_num)

# make space
def space():
    for i in range(3):
        st.write("")

# 被験者情報の入力
def department(dep_list):
    user_dep = st.selectbox("学科を選択してください", dep_list)
    st.sidebar.write("学科: " + user_dep)

# select
def selection():
    dice_face = st.empty()
    count = 75
    while count > 0:
        Q_num = random.randint(1, 126)
        dice_face.text(Q_num)
        #st.write(dice_face_num)
        if count < 10:
            time.sleep(0.5)
        else:
            time.sleep(0.1)

        count-=1

    return Q_num
        
############################## contents ##############################

img = Image.open('image_01.png')
st.image(img, use_column_width=True)

st.title("実験　第１部 & 第２部（prototype）")
space()

## 被験者情報の入力
st.header("【被験者情報の入力】")
user_ID = st.text_input("被験者番号を入力してください")
st.sidebar.write("被験者番号: " + user_ID)

user_name = st.text_input("名前を入力してください")
st.sidebar.write("被験者氏名: " + user_name)
space()

## 練習
st.header("【謝礼金の対象となる質問の決定　第一部（練習）】")
"""
こちらでは謝礼金の対象となった質問を決定する作業の練習ができます．
この練習では，決定（練習）のボタンを何度も押すことができます．
謝礼金の対象となる質問の決定（本番）でも，この練習と同一のアルゴリズムによって，
あなたの謝礼金の対象となる質問を決定します．
"""
space()


st.write("ボタンを押して練習してみましょう．")
train_button = st.button('決定（練習：何度でも押せます）')

if train_button:
    main(selection())

space()

## 本番
st.header("【謝礼金の対象となる質問の決定　第一部（本番）】")

if 'exp01' not in st.session_state:
    st.session_state.exp01 = 0

exp01_buttom = st.button('決定（本番：一度しか押せません）')

if exp01_buttom and st.session_state.exp01 == 0:
    st.session_state.exp01 = selection()

main(st.session_state.exp01)
space()

## 本番
st.header("【謝礼金の対象となる質問の決定　第二部（本番）】")
space()