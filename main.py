import streamlit as st
from PIL import Image
import random
import numpy as np
import time
import pandas as pd
import func as fc

# Page size
#st.set_page_config(layout="wide")


# Default values
Q_num = "-"
flag = 0
# Title 
st.title("実験タイトル")

# Input information about a subject 
st.header("【被験者情報の入力】")

user_ID = st.text_input("被験者番号を入力してください (半角数字)")
user_name = st.text_input("名前を入力してください")

st.sidebar.write("被験者番号: " + user_ID)
st.sidebar.write("被験者氏名: " + user_name)


### --- PART 1 --- ###
st.header("【第一部】")
st.sidebar.write("【第一部】---------------------------")
Q_num_1 = "-"
key = "-"
reward_01 = 0

# Decide question number
if 'Q_num_01' not in st.session_state:
    st.session_state.Q_num_01 = 0

exp01_buttom = st.button('質問番号の決定（第一部）')

if exp01_buttom and st.session_state.Q_num_01 == 0:
    st.session_state.Q_num_01 = fc.get_Q_num(1)

Q_num_1 = st.session_state.Q_num_01
st.sidebar.write(f"謝礼対象の質問番号: {Q_num_1}")

fc.space()


if st.session_state.Q_num_01:
    your_choice_dic = fc.get_choices(st.session_state.Q_num_01)

    keys = your_choice_dic.keys()
    choice_ls = ["選択してください"]
    for k in keys:
        choice_ls.append(k)

    key = st.selectbox("質問番号「 {}  」でのあなたの回答を選択してください".format(Q_num_1), choice_ls)

    if key != "選択してください":
        your_choice_num = your_choice_dic[key]

        if your_choice_num > 0 and flag == 0:
            reward_01 = fc.get_reward_01(Q_num_1, your_choice_num)
            flag +=1
            pg.main()


st.sidebar.write(f"{Q_num_1} でのあなたの回答: {key}")
st.sidebar.write(f"{Q_num_1} でのあなたの報酬: {int(reward_01)} 円")

### --- PART 2 --- ###
st.header("【第二部】")
st.sidebar.write("【第二部】---------------------------")
reward_02 = 0


# Decide question number
if 'Q_num_02' not in st.session_state:
    st.session_state.Q_num_02 = 0

exp02_buttom = st.button('質問番号の決定（第二部）')

if exp02_buttom and st.session_state.Q_num_02 == 0:
    st.session_state.Q_num_02 = fc.get_Q_num(2)

Q_num_2 = st.session_state.Q_num_02
st.sidebar.write(f"謝礼対象の質問番号: {Q_num_2}")


if st.session_state.Q_num_02:
    stock_A_num, stock_B_num, stock_C_num = 0,0,0

    # 選ばれた質問に対する証券の枚数を入力
    if st.session_state.Q_num_02 < 4:
        stock_A_num  = st.slider('証券Aの枚数', 0, 250, 0)
        stock_B_num = 250 - stock_A_num

        st.sidebar.write(f"証券Aの枚数: {stock_A_num}")
        st.sidebar.write(f"証券Bの枚数: {stock_B_num}")

        df_stock = pd.DataFrame([stock_A_num, stock_B_num,], index = ("証券A", "証券B",), columns=["枚数"])
        st.table(df_stock)

        reward_02 = 0
        reward_A = 10 * stock_A_num
        reward_02 += reward_A

        reward_B = fc.get_reward_B(st.session_state.Q_num_02, stock_B_num)
        if float(reward_B):
            reward_02 += reward_B


    elif 3 < st.session_state.Q_num_02 and st.session_state.Q_num_02 < 7:
        stock_A_num  = st.slider('証券Aの枚数', 0, 250, 0)
        stock_C_num = 250 - stock_A_num    

        st.sidebar.write(f"証券Aの枚数: {stock_A_num}")
        st.sidebar.write(f"証券Cの枚数: {stock_C_num}")

        df_stock = pd.DataFrame([stock_A_num, stock_C_num], index = ("証券A", "証券C"), columns=["枚数"])
        st.table(df_stock)

        reward_02 = 0
        reward_A = 10 * stock_A_num
        reward_02 += reward_A

        if stock_A_num != 250:
            red_ball_num = fc.get_red_num_box_C()
            reward_C = fc.get_reward_C(st.session_state.Q_num_02, stock_C_num, red_ball_num)
        else:
            reward_C = 0

        if float(reward_C):
            reward_02 += reward_C


    elif 6 < st.session_state.Q_num_02:
        stock_A_num  = st.slider('証券Aの枚数', 0, 250, 0)
        rest_num = 250 - stock_A_num

        if rest_num >0:
            stock_B_num  = st.slider('証券Bの枚数', 0, rest_num, 0)   
            stock_C_num = rest_num - stock_B_num
        
        else: 
            stock_B_num = 0
            stock_C_num = 0

        st.sidebar.write(f"証券Aの枚数: {stock_A_num}")
        st.sidebar.write(f"証券Bの枚数: {stock_B_num}")
        st.sidebar.write(f"証券Cの枚数: {stock_C_num}")

        df_stock = pd.DataFrame([stock_A_num, stock_B_num, stock_C_num], index = ("証券A", "証券B", "証券C"), columns=["枚数"])
        st.table(df_stock)

        reward_02 = 0
        reward_A = 10 * stock_A_num
        reward_02 += reward_A


        # Reward B
        if stock_A_num != 250:
            reward_B = fc.get_reward_B(st.session_state.Q_num_02, stock_B_num)

        else:
            reward_B = 0

        if float(reward_B):
            reward_02 += reward_B

        # Reward C
        if (stock_A_num + stock_B_num) != 250:
            red_ball_num = fc.get_red_num_box_C()
            reward_C = fc.get_reward_C(st.session_state.Q_num_02, stock_C_num, red_ball_num)

        else:
            reward_C = 0

        if float(reward_C):
            reward_02 += reward_C



st.sidebar.write(f"{Q_num_2} でのあなたの報酬: {int(reward_02)} 円")
