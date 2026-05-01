import streamlit as st

st.set_page_config(
    page_title="ハチの合格判定AI",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 ハチの合格判定AI")

try:
    st.image("image_0.png", width=200)
except:
    st.write("🐶 ハチ画像が表示できませんでした")

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

    if diff >= -5 and percent <= 10:
        result = "A判定"
        hachi_comment = "ハチ：すごい！かなり合格に近いワン！🐶✨"
        analysis = "高校偏差値と志望大学偏差値の差はありますが、学年順位がかなり上位です。今の努力を続ければ、十分に合格圏を狙えます。"
        advice = "過去問演習を増やして、得点の安定を目指しましょう。"

    elif diff >= -10 and percent <= 20:
        result = "B判定"
        hachi_comment = "ハチ：いい感じ！このまま頑張れば合格見えるワン！🐶"
        analysis = "志望大学との差は少しありますが、学年順位は上位です。苦手科目を減らせば、合格可能性はさらに高まります。"
        advice = "英語・数学など配点の高い科目を優先して強化しましょう。"

    elif diff >= -15 and percent <= 40:
        result = "C判定"
        hachi_comment = "ハチ：もう少し！あと一歩だワン！🐶💦"
        analysis = "現時点ではやや努力が必要な位置です。ただし、学年内で大きく遅れているわけではありません。"
        advice = "毎日の学習時間を固定し、基礎問題と過去問をバランスよく進めましょう。"

    else:
        result = "D判定"
        hachi_comment = "ハチ：まだ厳しいかも…でも伸びるワン！🐶🔥"
        analysis = "現在の条件では厳しめの判定です。ただし、今後の学習計画や科目対策で改善できる可能性はあります。"
        advice = "まずは志望校との差を確認し、基礎固めから計画的に進めましょう。"

    st.subheader(f"結果：{result}")

    if result == "A判定":
        st.success(hachi_comment)
    elif result == "B判定":
        st.info(hachi_comment)
    elif result == "C判定":
        st.warning(hachi_comment)
    else:
        st.error(hachi_comment)

    st.markdown("### AI風分析")
    st.write(analysis)

    st.markdown("### 次にやること")
    st.write(advice)

    st.divider()
    st.write(f"偏差値差：{diff}")
    st.write(f"学年上位：約 {percent:.1f}%")
