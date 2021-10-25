import streamlit as st
from PIL import Image
import random
import numpy as np
import time

st.set_page_config(layout="wide")

### 第一部 ###
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
    st.write("赤の玉出た場合の謝礼金： {a_red} 円".format(a_red = a_red))
    st.write("青の玉出た場合の謝礼金： {a_blue} 円".format(a_blue = a_blue))
    st.write("【あなたの回答が  {right_choice} の場合】".format(right_choice = Q_data[4]))
    st.write("{i} 円".format(i = i,))

    st.sidebar.write("第一部問題番号：【{Q_num}】".format(Q_num = Q_num))
    st.sidebar.write("【あなたの回答が  {left_choice} の場合】".format(left_choice = Q_data[3]))
    st.sidebar.write("使用する箱：箱B{box_num}".format(box_num = Q_data[2]))
    st.sidebar.write("赤の玉出た場合の謝礼金： {a_red} 円".format(a_red = a_red))
    st.sidebar.write("青の玉出た場合の謝礼金： {a_blue} 円".format(a_blue = a_blue))
    st.sidebar.write("【あなたの回答が  {right_choice} の場合】".format(right_choice = Q_data[4]))
    st.sidebar.write("{i} 円".format(i = i,))
    st.sidebar.write("---------------------------")


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
    st.write("赤の玉出た場合の謝礼金： {C_red} 円".format(C_red = C_red))
    st.write("青の玉出た場合の謝礼金： {C_blue} 円".format(C_blue = C_blue))
    st.write("")
    st.write("【あなたの回答が  {right_choice} の場合】".format(right_choice = Q_data[6]))
    st.write("箱Dから玉を一つ取り出します．")
    box_D(Q_num)
    st.write("赤の玉が出た場合： {D_red} 円".format(D_red = D_red))
    st.write("青の玉が出た場合： {D_blue} 円".format(D_blue = D_blue))


    st.sidebar.write("第一部問題番号：【{Q_num}】".format(Q_num = Q_num))
    st.sidebar.write("【あなたの回答が  {left_choice} の場合】".format(left_choice = Q_data[5]))
    st.sidebar.write("使用する箱：箱C{box_num}".format(box_num = Q_data[4],))
    st.sidebar.write("赤の玉出た場合の謝礼金： {C_red} 円".format(C_red = C_red))
    st.sidebar.write("青の玉出た場合の謝礼金： {C_blue} 円".format(C_blue = C_blue))
    st.write("")
    st.sidebar.write("【あなたの回答が  {right_choice} の場合】".format(right_choice = Q_data[6]))
    st.sidebar.write("使用する箱：箱D")
    st.sidebar.write("赤の玉が出た場合： {D_red} 円".format(D_red = D_red))
    st.sidebar.write("青の玉が出た場合： {D_blue} 円".format(D_blue = D_blue))
    st.sidebar.write("---------------------------")

    global cBox_check
    cBox_check =1

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
    count = 30
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

### 第二部 ###
def selection_02():
    dice_face = st.empty()
    count = 30
    
    while count > 0:
        Q_num = random.randint(1, 15)
        dice_face.text(Q_num)

        if count < 10:
            time.sleep(0.5)
        else:
            time.sleep(0.1)

        count-=1
    
    st.write(str(Q_num) + "が選ばれました.")
    return Q_num

def select_box(Q_num):
    dic = {
        
    1:   [ 'B', 1],
    2:   [ 'B', 2],
    3:   [ 'B', 3],
    4:   [ 'C', 1],
    5:   [ 'C', 2],
    6:   [ 'C', 3],
    7:   [ 'B', 1, 'C', 1,],
    8:   [ 'B', 1, 'C', 2,],
    9:   [ 'B', 1, 'C', 3,],
    10: [ 'B', 2, 'C', 1,],
    11: [ 'B', 2, 'C', 2,],
    12: [ 'B', 2, 'C', 3,],
    13: [ 'B', 3, 'C', 1,],
    14: [ 'B', 3, 'C', 2,],
    15: [ 'B', 3, 'C', 3,],
        
    }
    
    return dic[Q_num]

def stock_A(stock_num):
    price = 10
    return stock_num * price

def stock_B(stock_num, box_num):
    price = 10
    
    if box_num == 1:
        get_value = one(stock_num)
        red_price = get_value[0] * price
        blue_price = get_value[1] * price

    elif box_num == 2:
        get_value = two(stock_num)
        red_price = get_value[0] * price
        blue_price = get_value[1] * price
        
    elif box_num == 3:
        get_value = three(stock_num)
        red_price = get_value[0] * price
        blue_price = get_value[1] * price
    
    return red_price, blue_price

def stock_C(stock_num, box_num):
    price = 10
    
    if box_num == 1:
        get_value = one(stock_num)
        red_price = get_value[0] * price
        blue_price = get_value[1] * price

    elif box_num == 2:
        get_value = two(stock_num)
        red_price = get_value[0] * price
        blue_price = get_value[1] * price
        
    elif box_num == 3:
        get_value = three(stock_num)
        red_price = get_value[0] * price
        blue_price = get_value[1] * price
    
    global cBox_check
    cBox_check =1

    return red_price, blue_price



def one(num):
    #倍率
    red_multi = 1.2
    blue_multi = 0.9
    
    #金額
    red_price = num * red_multi
    blue_price = num * blue_multi
    
    return red_price, blue_price

def two(num):
    #倍率
    red_multi = 1.3
    blue_multi = 0.8
    
    #金額
    red_price = num * red_multi
    blue_price = num * blue_multi
    
    return red_price, blue_price

def three(num):
    #倍率
    red_multi = 1.4
    blue_multi = 0.7
    
    #金額
    red_price = num * red_multi
    blue_price = num * blue_multi
    
    return red_price, blue_price


def main_02(Q_num, box_info,):

    st.write()

    
    def main_02_A(Q_num, your_A, your_A_price):
        st.write("問題番号：【" + str(Q_num) + "】")
        st.write("【証券A " + str(your_A) + " 枚】")
        st.write(str(your_A_price) + "円")
        st.sidebar.write("第二部問題番号：【" + str(Q_num) + "】")
        st.sidebar.write("【証券A " + str(your_A) + " 枚】")
        st.sidebar.write(str(your_A_price) + "円")
        st.write("")
    
    if 1<= Q_num <=3:
        your_A = int(st.text_input('証券Aの購入枚数を入力してください。（0枚の場合は 0 を入力）'))
        your_A_price = stock_A(your_A)
        your_B = int(st.text_input("証券B" + str(box_info[1]) + "の購入枚数を入力してください。（0枚の場合は 0 を入力）"))
        your_B_price = stock_B(your_B, box_info[1])

        main_02_A(Q_num, your_A, your_A_price)
        st.write("【証券B" + str(box_info[1]) + " " + str(your_B) + " 枚】")
        st.write("箱B" + str(box_info[1]) + " から赤の玉が出た場合：" + str(int(your_B_price[0])) + "円" )
        st.write("箱B" + str(box_info[1]) + " から青の玉が出た場合：" + str(int(your_B_price[1])) + "円" )
        st.sidebar.write("【証券B" + str(box_info[1]) + " " + str(your_B) + " 枚】")
        st.sidebar.write("赤の玉が出た場合：" + str(int(your_B_price[0])) + "円" )
        st.sidebar.write("青の玉が出た場合：" + str(int(your_B_price[1])) + "円" )

    elif 4<= Q_num <=6:
        your_A = int(st.text_input('証券Aの購入枚数を入力してください。（0枚の場合は 0 を入力）'))
        your_A_price = stock_A(your_A)
        your_C = int(st.text_input("証券C" + str(box_info[1]) + "の購入枚数を入力してください。（0枚の場合は 0 を入力）"))
        your_C_price = stock_C(your_C, box_info[1]) #箱Cの番号がリスト2番目なのに注意

        main_02_A(Q_num, your_A, your_A_price)
        st.write("【証券C" + str(box_info[1]) + " " + str(your_C) + " 枚】")
        st.write("箱C" + str(box_info[1]) + " から赤の玉が出た場合：" + str(int(your_C_price[0])) + "円" )
        st.write("箱C" + str(box_info[1]) + " から青の玉が出た場合：" + str(int(your_C_price[1])) + "円" )
        st.sidebar.write("【証券C" + str(box_info[1]) + " " + str(your_C) + " 枚】")
        st.sidebar.write("赤の玉が出た場合：" + str(int(your_C_price[0])) + "円" )
        st.sidebar.write("青の玉が出た場合：" + str(int(your_C_price[1])) + "円" )
        
    elif 7<= Q_num <=15:
        your_A = int(st.text_input('証券Aの購入枚数を入力してください。（0枚の場合は 0 を入力）'))
        your_A_price = stock_A(your_A)
        your_B = int(st.text_input("証券B" + str(box_info[1]) + "の購入枚数を入力してください。（0枚の場合は 0 を入力）"))
        your_C = int(st.text_input("証券C" + str(box_info[3]) + "の購入枚数を入力してください。（0枚の場合は 0 を入力）"))
        your_B_price = stock_B(your_B, box_info[1])
        your_C_price = stock_C(your_C, box_info[3])
        
        main_02_A(Q_num, your_A, your_A_price)
        st.write("【証券B" + str(box_info[1]) + " " + str(your_B) + " 枚】")
        st.write("箱B" + str(box_info[1]) + " から赤の玉が出た場合：" + str(int(your_B_price[0])) + "円" )
        st.write("箱B" + str(box_info[1]) + " から青の玉が出た場合：" + str(int(your_B_price[1])) + "円" )
        st.write("")
        st.write("【証券C" + str(box_info[1]) + " " + str(your_C) + " 枚】")
        st.write("箱C" + str(box_info[1]) + " から赤の玉が出た場合：" + str(int(your_C_price[0])) + "円" )
        st.write("箱C" + str(box_info[1]) + " から青の玉が出た場合：" + str(int(your_C_price[1])) + "円" )
        st.sidebar.write("【証券B" + str(box_info[1]) + " " + str(your_B) + " 枚】")
        st.sidebar.write("赤の玉が出た場合：" + str(int(your_B_price[0])) + "円" )
        st.sidebar.write("青の玉が出た場合：" + str(int(your_B_price[1])) + "円" )
        st.sidebar.write("【証券C" + str(box_info[1]) + " " + str(your_C) + " 枚】")
        st.sidebar.write("赤の玉が出た場合：" + str(int(your_C_price[0])) + "円" )
        st.sidebar.write("青の玉が出た場合：" + str(int(your_C_price[1])) + "円" )

    st.write("")

## dice
# Functions
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

# make space
def space():
    for i in range(3):
        st.write("")

############################## contents ##############################
cBox_check = 0

#img = Image.open('image_01.png')
#st.image(img, use_column_width=True)

st.title("実験　第１部 & 第２部")
space()

## 練習ページへのリンク
st.header("【練習ページへのリンク】")
st.write("https://share.streamlit.io/kt0zuka/train-risk_appetite-2021/main/main.py")
st.write("")

## 被験者情報の入力
st.header("【被験者情報の入力】")
user_ID = st.text_input("被験者番号を入力してください")
st.sidebar.write("被験者番号: " + user_ID)

user_name = st.text_input("名前を入力してください")
st.sidebar.write("被験者氏名: " + user_name)
st.sidebar.write("---------------------------")
space()


## 本番
st.header("【謝礼金の対象となる質問の決定　第一部】")

space()

if 'exp01' not in st.session_state:
    st.session_state.exp01 = 0

exp01_buttom = st.button('決定（第一部）')

if exp01_buttom and st.session_state.exp01 == 0:
    st.session_state.exp01 = selection()

main(st.session_state.exp01)
space()

## 本番
st.header("【謝礼金の対象となる質問の決定　第二部】")
st.write("※エラーが表示される場合がありますが，実験において問題ないため気にせず進めてください．")
space()

a = 0
b = 0

if 'exp02' not in st.session_state:
    st.session_state.exp02 = 0

if 'exp02_box' not in st.session_state:
    st.session_state.exp02_box = 0

exp02_switch = st.button('決定（第二部）')

if exp02_switch and st.session_state.exp02 == 0:
    st.session_state.exp02 = selection_02()
    a +=1

if exp02_switch and st.session_state.exp02_box == 0:
    st.session_state.exp02_box = select_box(st.session_state.exp02)
    b +=1

main_02(st.session_state.exp02, st.session_state.exp02_box)


space()

#if cBox_check ==1:
    #st.write("あなたの謝礼金額の決定には，箱Cを作成する必要があります．")
    #st.write("リンク先へ進んで，箱C作成へ進んでください．https://share.streamlit.io/kt0zuka/dice/main.py")


### dice contents ###

if cBox_check ==1:
    st.sidebar.write("---------------------------")
    st.sidebar.write("箱C1~C3の作成")
    st.header("【箱C1~C3の作成】")
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

    dice_num_button = st.button('サイコロを振る（サイコロの数の決定）')

    if dice_num_button and st.session_state.dice_num == 0:

        st.session_state.dice_num = dice(6)

    st.image('6dice_{num}.png'.format( num = st.session_state.dice_num ) )

    st.write("出目は「　" + str(st.session_state.dice_num) + "　」でした。")
    st.write("あなたが振るサイコロの数は「　" + str(st.session_state.dice_num) + "　」個です。")
    st.sidebar.write("サイコロの数：" + str(st.session_state.dice_num) + " 個")

    space()

    ## 2. 被験者が振るダイスの面体を決める -----------------------------------------------------------------------------------------
    st.subheader("2. 被験者が振るサイコロの面体を決める")

    face_list = [4, 6, 8, 10, 12, 24, 30, 100]
    face_dic = {0:0, 4:1, 6:2, 8:3, 10:4, 12:5, 24:6, 30:7, 100:8}

    if 'face_num' not in st.session_state:
        st.session_state.face_num = 0

    face_num_button = st.button('サイコロを振る（サイコロの面体の決定）')

    if face_num_button and st.session_state.face_num == 0:

        st.session_state.face_num = random.choice( face_list )

    st.image('8dice_{num}.png'.format( num = face_dic[st.session_state.face_num] ) )

    st.write("出目は「　" + str(face_dic[st.session_state.face_num]) + "　」でした。")
    st.write("出目が「　" + str(face_dic[st.session_state.face_num]) + "　」なので、サイコロの種類は「　" + str(st.session_state.face_num) + "　」面体です。")
    st.sidebar.write("サイコロの種類： " + str(st.session_state.face_num) + " 面体")

    st.write("")

    st.write("あなたは「　 {face}　」 面体サイコロを「　 {dice}　」 回振ることになりました。".format( dice = st.session_state.dice_num, face =st.session_state.face_num))

    space()

    ## 3. 被験者が謝礼金決定に用いる赤玉の数を決める -----------------------------------------------------------------------------------------
    st.subheader("3. 被験者が謝礼金決定に用いる赤玉の数を決める")
    st.write("ボタンを押すと {face} 面体サイコロを {dice} 個振ることができます。".format( dice = st.session_state.dice_num, face =st.session_state.face_num))

    your_sum = 0

    if 'sum_value' not in st.session_state:
        st.session_state.sum_value = 0

    sum_value_button = st.button('サイコロを振る（赤い玉の決定）')

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

        space()

        st.write("以上で赤い玉の数を決める作業は終了です。")
        st.write("実験者に赤い玉の数を伝え、謝礼金額の決定に進んで下さい。")
