import streamlit as st
import yfinance as yf

st.write("""
# My first app
Hello *world!*
""")
df = yf.download("AAPL", start="2010-11-01", end="2020-11-01", progress=False)
st.line_chart(df)
