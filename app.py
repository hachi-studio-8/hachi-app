import streamlit as st

st.title("🐶 ハチ式 合格判定AI")

st.write("偏差値と順位から合格可能性を判定します")

school = st.slider("高校の偏差値", 30, 80, 60)
target = st.slider("志望大学の偏差値", 30, 80, 65)
rank = st.number_input("学年順位", 1, 500, 50)
total = st.number_input("学年人数", 1, 500, 200)

if st.button("判定する"):
    score = school - target + (1 - rank/total) * 20

    if score > 10:
        result = "A判定"
    elif score > 5:
        result = "B判定"
    elif score > 0:
        result = "C判定"
    else:
        result = "D判定"

    st.subheader(f"結果：{result}")
