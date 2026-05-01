import streamlit as st

st.set_page_config(page_title="合格判定AIシミュレーター", page_icon="🐕")

st.title("🐕 合格判定AIシミュレーター!")

try:
    st.image("image_0.png", width=180)
except:
    st.write("🐕 ハチ画像を表示できませんでした")

st.write("高校偏差値・学年順位・志望大学偏差値から、合格可能性を判定します。")

hachi_mode = st.radio(
    "ハチの性格を選んでください",
    ["やさしいハチ", "きびしいハチ", "戦略家ハチ"]
)

high_school_dev = st.number_input("高校の偏差値", min_value=30, max_value=80, value=60)
univ_dev = st.number_input("志望大学の偏差値", min_value=35, max_value=80, value=60)
grade_rank = st.number_input("学年順位（例：1位なら1）", min_value=1, max_value=500, value=50)
students = st.number_input("学年人数", min_value=1, max_value=1000, value=200)

rank_rate = grade_rank / students
dev_gap = high_school_dev - univ_dev
score = dev_gap

# 学年順位による補正
if rank_rate <= 0.05:
    score += 10
elif rank_rate <= 0.10:
    score += 7
elif rank_rate <= 0.20:
    score += 4
elif rank_rate <= 0.35:
    score += 1
elif rank_rate >= 0.80:
    score -= 8
elif rank_rate >= 0.60:
    score -= 5
elif rank_rate >= 0.45:
    score -= 2

possibility = 50 + score * 5
possibility = max(5, min(95, possibility))

def make_base_comment(possibility, dev_gap, rank_rate):
    parts = []

    if possibility >= 80:
        parts.append("かなり有望だワン！合格圏にしっかり近づいているワン。")
    elif possibility >= 65:
        parts.append("十分に勝負できる位置だワン。ここからの仕上げが大事だワン。")
    elif possibility >= 45:
        parts.append("まだ可能性はあるワン。ただし安心するにはもう一段の努力が必要だワン。")
    else:
        parts.append("今のままだと厳しめだワン。でも、ここから作戦を立てればまだ伸ばせるワン。")

    if dev_gap >= 5:
        parts.append("高校偏差値が志望大学偏差値を上回っているので、学力面では有利な材料があるワン。")
    elif dev_gap >= 0:
        parts.append("高校偏差値と志望大学偏差値が近いので、日々の成績と過去問対策が勝負を分けるワン。")
    elif dev_gap >= -5:
        parts.append("志望大学の方が少し高めなので、苦手科目を放置すると危ないワン。")
    else:
        parts.append("志望大学の難度がかなり高めだワン。基礎固めから得点源作りまで、計画的に進める必要があるワン。")

    if rank_rate <= 0.05:
        parts.append("学年トップ層なのは大きな強みだワン。自信を持っていいワン。")
    elif rank_rate <= 0.10:
        parts.append("学年上位に入っているので、かなり良い材料だワン。")
    elif rank_rate <= 0.30:
        parts.append("順位は悪くないワン。ここから上位層に近づくと一気に有利になるワン。")
    elif rank_rate <= 0.50:
        parts.append("学年順位は中位なので、まずは上位3割を目標にすると良いワン。")
    else:
        parts.append("順位面ではまだ課題があるワン。毎日の復習と基礎問題の取りこぼし対策が重要だワン。")

    return parts

def make_hachi_comment(mode, possibility, dev_gap, rank_rate):
    parts = make_base_comment(possibility, dev_gap, rank_rate)

    if mode == "やさしいハチ":
        parts.append("大丈夫だワン。今の結果はゴールじゃなくて、次に進むための地図だワン。焦らず一歩ずつ進めば、必ず力はついてくるワン。")
    elif mode == "きびしいハチ":
        parts.append("正直に言うワン。今のまま何となく勉強しても大きくは変わらないワン。苦手を見つけて、毎日やることを決めるワン。")
    else:
        parts.append("戦略的にいくワン。まず苦手科目を1つ選ぶ。次に過去問を1年分確認する。そして毎日30分、同じ時間に続けるワン。")

    return "\n\n".join(parts)

def make_next_target(possibility):
    if possibility < 65:
        need_score = 65 - possibility
        need_dev = int((need_score + 4) // 5)
        return f"B判定に近づくには、目安として偏差値をあと約{need_dev}上げるか、学年順位をもう一段上げたいワン。"
    elif possibility < 80:
        need_score = 80 - possibility
        need_dev = int((need_score + 4) // 5)
        return f"A判定に近づくには、目安として偏差値をあと約{need_dev}上げたいワン。"
    else:
        return "今はかなり良い位置だワン。ここからは過去問演習と本番対策で安定感を高めるワン。"

def make_school_level_advice(possibility):
    if possibility >= 80:
        return "安全圏〜実力相応校だワン。今の志望校は十分に現実的だワン。さらに上の大学を挑戦校として考えてもいいワン。"
    elif possibility >= 65:
        return "実力相応校だワン。合格の可能性は十分あるけれど、油断すると危ない位置だワン。今の志望校を本命にしてよいワン。"
    elif possibility >= 45:
        return "挑戦校だワン。届かないわけではないけれど、今のままだと少し不安があるワン。併願校として少し下の大学も考えると安心だワン。"
    else:
        return "かなり高い挑戦校だワン。目標としては良いけれど、現実的には安全校・実力相応校も必ず用意した方がいいワン。"

def make_school_level_table(univ_dev):
    safe = max(35, univ_dev - 8)
    suitable_low = max(35, univ_dev - 4)
    suitable_high = univ_dev
    challenge_low = univ_dev + 1
    challenge_high = min(80, univ_dev + 5)

    return f"""
### 志望校レベルの目安

| 区分 | 偏差値の目安 | 考え方 |
|---|---:|---|
| 安全圏 | {safe}〜{suitable_low - 1} | 合格を取りに行く大学 |
| 実力相応 | {suitable_low}〜{suitable_high} | 本命にしやすい大学 |
| 挑戦校 | {challenge_low}〜{challenge_high} | 努力次第で狙う大学 |
| かなり高い挑戦校 | {challenge_high + 1}以上 | 強い対策が必要な大学 |
"""

if st.button("判定する"):
    st.subheader("判定結果")

    if possibility >= 80:
        result = "A判定"
        color = "green"
    elif possibility >= 65:
        result = "B判定"
        color = "blue"
    elif possibility >= 45:
        result = "C判定"
        color = "orange"
    else:
        result = "D判定"
        color = "red"

    st.markdown(f"## :{color}[{result}]")
    st.markdown(f"## 合格可能性：:{color}[{int(possibility)}％]")
    st.progress(int(possibility))

    st.write(f"### 🐕 {hachi_mode} のコメント")
    st.info(make_hachi_comment(hachi_mode, possibility, dev_gap, rank_rate))

    st.write("### 次の目標")
    st.success(make_next_target(possibility))

    st.write("### 志望校レベル提案")
    st.warning(make_school_level_advice(possibility))
    st.markdown(make_school_level_table(univ_dev))

    st.write("### 判定の理由")
    st.write(f"高校偏差値：{high_school_dev}")
    st.write(f"志望大学偏差値：{univ_dev}")
    st.write(f"偏差値差：{dev_gap}")
    st.write(f"学年順位：{grade_rank}位 / {students}人中")
