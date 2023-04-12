import streamlit as st
from PIL import Image

st.title("打ち込み最適化アプリ")
st.caption("これは打ち込み順序を計算するアプリです")

image = Image.open('./data/コンパス.png')
st.image(image, width=500)
