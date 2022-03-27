import streamlit as st
from PIL import Image
import random
import numpy as np
import time
import pandas as pd
import progress_bar as pb

# make space
def space():
    for i in range(3):
        st.write("")


# Decide question number (partnum: 1 = 147, 2 = 15)
def get_Q_num(part_num):
    Q_num_dic = {1:147, 2:15}
    dice_face = st.empty()
    count = 30
    while count > 0:
        Q_num = random.randint(1, Q_num_dic[part_num])
        dice_face.text("あなたの質問番号は：「　{}　」".format(Q_num))
        #st.write(dice_face_num)
        if count < 10:
            time.sleep(0.5)
        else:
            time.sleep(0.1)

        count-=1

    return Q_num


def get_choices(Q_num=0):

    if 1 <= Q_num <= 5: #question 1
        choice_dic = {'ア': 2 , 'イ': 1}

    elif 6 <= Q_num <= 12: #question 2
        choice_dic = {'ウ': 2 , 'エ': 1}

    elif 13 <= Q_num <= 21: #question 3
        choice_dic = {'オ': 2 , 'カ': 1}
    
    elif 22 <= Q_num <= 42: #question 4
        choice_dic = {'キ': 3 , 'ク': 4}

    elif 43 <= Q_num <= 63: #question 5
        choice_dic = {'ケ': 3 , 'コ': 4}

    elif 64 <= Q_num <= 84: #question 6
        choice_dic = {'サ': 3 , 'シ': 4}

    elif 85 <= Q_num <= 105: #question 7
        choice_dic = {'ス': 3 , 'セ': 4}

    elif 106 <= Q_num <= 126: #question 8
        choice_dic = {'ソ': 3 , 'タ': 4}

    elif 127 <= Q_num <= 147: #question 9
        choice_dic = {'チ': 3 , 'ツ': 4}

    else:
        choice_dic = {'-': 0}

    return choice_dic


def stock_A(Q_num, stock_A_num=0): # 第二部の場合、第二引数に証券Aの枚数を渡す

    price = 10

    if stock_A_num ==0: # Question 1
        dic = {1:175, 2:185, 3:195, 4:205, 5:215,
            6:155, 7:165, 8:175, 9:185, 10:195, 11:205, 12:215,
            13:135, 14:145, 15:155, 16:165, 17:175, 18:185, 19:195, 20:205, 21:215,}
        
        stock_A_num = dic[Q_num]
    
    sum = price * stock_A_num
    return sum

def box(Q_num, red_ball_num=50):

    def get_multi(Q_num):
        if Q_num in range(1, 6) or Q_num in range(22, 43) or Q_num in range(43, 64):
            ls =  [1.2, 0.9]
            if Q_num in range(43, 64):
                ls = list(reversed(ls))
        
        elif Q_num in range(6, 13) or Q_num in range(64, 85) or Q_num in range(85, 106):
            ls =  [1.3, 0.8]
            if Q_num in range(85, 106):
                ls = list(reversed(ls))

        elif Q_num in range(13, 22) or Q_num in range(106, 127) or Q_num in range(127, 148):
            ls =  [1.4, 0.7]
            if Q_num in range(127, 148):
                ls = list(reversed(ls))

        return ls

    multi_ls = get_multi(Q_num)
    multi_dic = {"red": multi_ls[0],"blue": multi_ls[1]}
    price = 10
    stock_num = 200

    red_price = (price * multi_dic['red']) * stock_num
    blue_price = (price * multi_dic['blue']) * stock_num

    ball = pb.box(red_ball_num) #dummy

    if ball==0:
        reward = red_price
    elif ball==1:
        reward = blue_price

    return reward


# Dice
def dice(input_face_num):
    if input_face_num == 10:
        return random.randint(0, 9)
    else:
        return random.randint(1, input_face_num)

# Get the number of red balls
def get_value(sum):
    if sum < 10:
        return sum
    else:
        if sum % 2 == 0:
            tens_place = str(sum)[-1]
            ones_place = str(sum)[-2]
            return int( tens_place + ones_place )
        else:
            tens_place = str(sum)[-2]
            ones_place = str(sum)[-1]
            return int( tens_place + ones_place )


def get_red_num_box_C():

    #st.sidebar.write("---------------------------")
    #st.sidebar.write("箱C1~C3の作成")
    st.write("---------------------------")
    st.subheader("【箱C1~C3の作成】")
    st.write("")
    process_txt = """
    ### 具体的な流れ
    #### 1. 被験者が振るサイコロの数を決める: n
    使用するのは６面体のダイス
    - 被験者は１〜６個のいずれかの数のサイコロを振ることになる
    #### 2. 被験者が振るサイコロの面体を決める: m
    使用するのは８面体のダイス
    - 出目が１ならば　４面体
    - 出目が２ならば　６面体
    - 出目が３ならば　８面体
    - 出目が４ならば　１０面体
    - 出目が５ならば　１２面体
    - 出目が６ならば　２４面体
    - 出目が７ならば　３０面体
    - 出目が８ならば　１００面体
    #### 3. 被験者が謝礼金決定に用いる赤玉の数を決める: Z
    - m 面体のサイコロを n 個振り、出目の合計を得る
    - 出目の合計が偶数の場合
        - 下3桁から3桁目、2桁目の順で数字を読む
        - 例）428→82
    - 出目の合計が奇数の場合
        - 下2桁とする
        - 例）429→29
    """
    st.subheader("＜箱C1~C3の作成・謝礼金の決定について＞")
    st.write("下記をクリックしてお読みください．")

    process = st.expander("具体的な流れ")
    process.write(process_txt)

    st.write()

    st.subheader("＜赤い玉の数を決める作業＞")
    st.write("※　各ボタンはそれぞれ１度だけ押すことができます。")
    st.write("")
    ## 1. 振るダイスの数を決める -----------------------------------------------------------------------------------------
    st.subheader("1. 振るサイコロの数を決める")


    if 'dice_num' not in st.session_state:
        st.session_state.dice_num = 0

    dice_num_button = st.button('サイコロの数の決定')

    if dice_num_button and st.session_state.dice_num == 0:

        st.session_state.dice_num = dice(6)

    st.image('6dice_{num}.png'.format( num = st.session_state.dice_num ) )

    st.write("出目は「　" + str(st.session_state.dice_num) + "　」でした。")
    st.write("あなたが振るサイコロの数は「　" + str(st.session_state.dice_num) + "　」個です。")
    #st.sidebar.write("サイコロの数：" + str(st.session_state.dice_num) + " 個")
    yourdice_num = st.session_state.dice_num

    space()

    ## 2. 被験者が振るダイスの面体を決める -----------------------------------------------------------------------------------------
    st.subheader("2. 被験者が振るサイコロの面体を決める")

    face_list = [4, 6, 8, 10, 12, 24, 30, 100]
    face_dic = {0:0, 4:1, 6:2, 8:3, 10:4, 12:5, 24:6, 30:7, 100:8}

    if 'face_num' not in st.session_state:
        st.session_state.face_num = 0

    face_num_button = st.button('サイコロの面体の決定')

    if face_num_button and st.session_state.face_num == 0:

        st.session_state.face_num = random.choice( face_list )

    st.image('8dice_{num}.png'.format( num = face_dic[st.session_state.face_num] ) )

    st.write("出目は「　" + str(face_dic[st.session_state.face_num]) + "　」でした。")
    st.write("出目が「　" + str(face_dic[st.session_state.face_num]) + "　」なので、サイコロの種類は「　" + str(st.session_state.face_num) + "　」面体です。")
    st.sidebar.write("サイコロの種類： " + str(st.session_state.face_num) + " 面体")

    st.write("")

    st.write("あなたは「　 {face}　」 面体サイコロを「　 {dice}　」 回振ることになりました。".format( dice = st.session_state.dice_num, face =st.session_state.face_num))
    yourdice_face = st.session_state.face_num
    #dl_table_on += 1
    space()

    ## 3. 被験者が謝礼金決定に用いる赤玉の数を決める -----------------------------------------------------------------------------------------
    st.subheader("3. 被験者が謝礼金決定に用いる赤玉の数を決める")
    st.write("ボタンを押すと {face} 面体サイコロを {dice} 個振ることができます。".format( dice = st.session_state.dice_num, face =st.session_state.face_num))

    your_sum = 0
    if 'sum_value' not in st.session_state:
        st.session_state.sum_value = 0

    sum_value_button = st.button('赤い玉の決定')

    if sum_value_button and st.session_state.sum_value == 0:
        st.write("")

        for i in range(st.session_state.dice_num):
            a = dice(st.session_state.face_num)
            your_sum += a
            st.write("{i} 個目：　出目は「　{a}　」でした。　現在の合計は「　{your_sum}　」です。".format( i = i+1, a=a, your_sum = your_sum ))
            time.sleep(0.5)
            if i == (st.session_state.dice_num - 1):
                st.write("全てのサイコロを振り終わりました。")

        st.session_state.sum_value = your_sum
        st.write("")

        st.write("{face} 面体サイコロを {dice} 個振った結果、出目の合計は「　".format( dice = st.session_state.dice_num, face =st.session_state.face_num) + str(st.session_state.sum_value)+ "　」でした。")
        st.write("謝礼金を決定するために用いる赤い玉の数を算出します。")
        time.sleep(1.0)
    space()

    red_balls_num = get_value( st.session_state.sum_value )

    if red_balls_num !=0:
        st.header("赤い玉の数は「　" + str(red_balls_num) + "　」個となりました。")
        st.sidebar.write("赤い玉の数: " + str(red_balls_num) + " 個")
        #st.sidebar.write("---------------------------")
        blue_balls_num = 100 - get_value(st.session_state.sum_value)

        st.write("以上で赤い玉の数を決める作業は終了です。")
        st.write("実験者に赤い玉の数を伝え、謝礼金額の決定に進んで下さい。")
    
    st.write("---------------------------")

    return red_balls_num

def get_red_num_box_D(Q_num):
    
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
    red_ball_num = dic[Q_num]
    return red_ball_num



def get_reward_01(Q_num, your_choice_num):
    Q_num = 30
    your_choice_num = 4
    your_reward = 0

    if your_choice_num == 1: # 証券A
        your_reward = stock_A(Q_num)

    elif your_choice_num == 2: # 証券B
        get_ball_button = st.button("ボールを取り出す")
        
        if get_ball_button:
            your_reward = box(Q_num)

    elif your_choice_num == 3: # 証券C
        # make box C and get a ball from box C
        red_ball_num = get_red_num_box_C()
        get_ball_button = st.button("ボールを取り出す")

        if get_ball_button:
            your_reward = box(Q_num, red_ball_num)

    elif your_choice_num == 4: #証券D
        # make box D and get a ball from box D
        red_ball_num = get_red_num_box_D(Q_num)
        get_ball_button = st.button("ボールを取り出す")

        if get_ball_button:
            your_reward = box(Q_num, red_ball_num)
    
    return your_reward

def get_reward_B(Q_num, stock_B_num, red_ball_num=50):
    reward = 0

    if Q_num in [4,5,6]:
        reward = 0

    else:
        dic = {
        1 : [1.2, 0.9], 2 : [1.3, 0.8], 3 : [1.4, 0.7],
        7 : [1.2, 0.9], 8 : [1.2, 0.9], 9 : [1.2, 0.9],
        10: [1.3, 0.8], 11: [1.3, 0.8], 12: [1.3, 0.8],
        13: [1.4, 0.7], 14: [1.4, 0.7], 15: [1.4, 0.7],
        }

        get_ball_button = st.button("ボールを取り出す（証券B）")
        if get_ball_button:
            multi_ls = dic[Q_num]
            multi_dic = {"red": multi_ls[0],"blue": multi_ls[1]}
            price = 10

            red_price = (price * multi_dic['red']) * stock_B_num
            blue_price = (price * multi_dic['blue']) * stock_B_num

            ball = pb.box(red_ball_num) #red = 50 in Box B

            if ball==0:
                reward = red_price
            elif ball==1:
                reward = blue_price

    return reward

def get_reward_C(Q_num, stock_C_num, red_ball_num):
    reward = 0

    if Q_num in [1,2,3]:
        reward = 0

    else:
    
        dic = {
        4 : [1.2, 0.9], 5 : [1.3, 0.8], 6 : [1.4, 0.7],
        7 : [1.2, 0.9], 8 : [1.3, 0.8], 9 : [1.4, 0.7],
        10: [1.2, 0.9], 11: [1.3, 0.8], 12: [1.4, 0.7],
        13: [1.2, 0.9], 14: [1.3, 0.8], 15: [1.4, 0.7],
        }

        get_ball_button = st.button("ボールを取り出す（証券C）")

        if get_ball_button:
            multi_ls = dic[Q_num]
            multi_dic = {"red": multi_ls[0],"blue": multi_ls[1]}
            price = 10

            red_price = (price * multi_dic['red']) * stock_C_num
            blue_price = (price * multi_dic['blue']) * stock_C_num

            ball = pb.box(red_ball_num) #red = 50 in Box B

            if ball==0:
                reward = red_price
            elif ball==1:
                reward = blue_price

    return reward
