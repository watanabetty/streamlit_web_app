import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# データ処理
df = pd.read_csv('./data/temperture.csv', index_col='月')
st.dataframe(df)
st.table(df)
st.line_chart(df)
st.bar_chart(df['2022年'])

fig, ax = plt.subplots()
ax.plot(df.index, df['2022年'])
ax.set_title('pyplot_graph')
st.pyplot(fig)