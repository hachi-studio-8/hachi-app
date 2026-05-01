import streamlit as st

st.set_page_config(
    page_title="ハチの合格判定AI",
    page_icon="🐶",
    layout="centered"
)

st.title("🎓 ハチの合格判定AI")

st.image("image_0.png", width=200)

st.write("高校の偏差値・志望大学の偏差値・学年順位から、合格可能性を判定します。")
st.warning("※これは学習用の簡易シミュレーターです。実際の合否を保証するものではありません。")

st.divider()

school_score = st.slider("高校の偏差値", 30, 80, 65)
target_score = st.slider("志望大学の偏差値", 30, 80, 70)

rank = st.number_input("学年順位", 1, 500, 20)
total_students = st.number_input("学年人数", 1, 1000, 200)

if st.button("判定する"):
    percent = (rank / total_students) * 100
    diff = school_score - target_score

    if diff >= 5 and percent <= 10:
        result = "A判定"
    elif diff >= 0 and percent <= 20:
        result = "B判定"
    elif diff >= -5 and percent <= 40:
        result = "C判定"
    else:
        result = "D判定"

    st.subheader(f"結果：{result}")
    st.write(f"偏差値差：{diff}")
    st.write(f"学年上位：約 {percent:.1f}%")
