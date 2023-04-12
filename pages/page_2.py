import streamlit as st
import streamlit as st
import datetime

with st.form(key="profile_form"):
    name2 = st.text_input("名前2")
    address2 = st.text_input("住所2")

    # セレクトボタン
    age_category = st.selectbox("年齢",
                                {"18才以上", "18才未満"})

    # ラジオボタン
    sex = st.radio("性別",
                   ("男", "女", "その他"),
                   horizontal=True)

    # マルチセレクト
    hoby = st.multiselect('趣味',
                          ('サッカー', '読書', '睡眠', '料理', 'ゲーム'))

    # チェックボックス
    select = st.checkbox("購入希望")

    # スライダー
    max_min = st.slider('身長', min_value=160, max_value=195)

    submit_btn2 = st.form_submit_button("送信")
    cancel_btn2 = st.form_submit_button("キャンセル")
    # print(f'submit_btn:{submit_btn2}')
    # print(f'cancel_btn:{cancel_btn2}')

    if submit_btn2:
        st.text(f"ようこそ{name2}さん！！")
        st.text(f"年齢層：{age_category}")
        st.text(f"性別区分：{sex}")
        st.text(f'趣味：{", ".join(hoby)}')

# 日付
day = datetime.date.today()
date = st.date_input('Input date')
# 入力の最大値・最小値指定も可能
date2 = st.date_input('Input date',
                      min_value=datetime.date(1900, 1, 1),
                      max_value=day,
                      value=datetime.date(2000, 1, 1))