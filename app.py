import streamlit as st

st.title("BoltPro")

name = st.text_input("ชื่อ")

if st.button("กด"):
    st.success(f"สวัสดี {name}")