import streamlit as st

st.set_page_config(
    page_title="ハチの合格判定AI",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 ハチの合格判定AI")

# ハチ画像
try:
    st.image("image_0.png", width=200)
except:
    st.write("🐶 ハチ画像が表示できませんでした")

st.write("高校の偏差値・志望大学の偏差値・学年順位から、合格可能性を判定します。")
st.warning("※これは学習用の簡易シミュレーターです。実際の合否を保証するものではありません。")

st.divider()

# 入力
school_score = st.slider("高校の偏差値", 30, 80, 65)
target_score = st.slider("志望大学の偏差値", 30, 80, 70)

rank = st.number_input("学年順位", 1, 500, 20)
total_students = st.number_input("学年人数", 1, 1000, 200)

# 判定
if st.button("判定する"):

    percent = (rank / total_students) * 100
    diff = school_score - target_score

    # 判定ロジック
    if diff >= -5 and percent <= 10:
        result = "A判定"
    elif diff >= -10 and percent <= 20:
        result = "B判定"
    elif diff >= -15 and percent <= 40:
        result = "C判定"
    else:
        result = "D判定"

    # 結果表示
    st.subheader(f"結果：{result}")

    # ハチコメント
    if result == "A判定":
        st.success("ハチ：すごい！かなり合格に近いワン！🐶✨")

    elif result == "B判定":
        st.info("ハチ：いい感じ！このまま頑張れば合格見えるワン！🐶")

    elif result == "C判定":
        st.warning("ハチ：もう少し！あと一歩だワン！🐶💦")

    else:
        st.error("ハチ：まだ厳しいかも…でも伸びるワン！🐶🔥")
