import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

def judge():
    try:
        hs = float(entry_hs.get())
        us = float(entry_us.get())
        rank = float(entry_rank.get())
        total = float(entry_total.get())

        diff = hs - us
        rank_rate = rank / total

        # 順位補正：上位ほど強く加点
        if rank_rate <= 0.01:
            rank_bonus = 10
        elif rank_rate <= 0.05:
            rank_bonus = 7
        elif rank_rate <= 0.10:
            rank_bonus = 4
        elif rank_rate <= 0.20:
            rank_bonus = 2
        else:
            rank_bonus = 0

        score = diff + rank_bonus
        
        if score >= 5:
            result = "A（合格可能性80%以上）"
        elif score >= 2:
            result = "B（合格可能性60%）"
        elif score >= 0:
            result = "C（五分五分）"
        elif score >= -3:
            result = "D（やや厳しい）"
        else:
            result = "E（かなり厳しい）"

        messagebox.showinfo("判定結果", result)

    except:
        messagebox.showerror("エラー", "数値を正しく入力してください")

root = tk.Tk()
root.title("大学合格判定アプリ")
root.geometry("520x620")
root.configure(bg="#FDF6ED")

# ハチ画像
try:
    image_path = os.path.join(os.path.dirname(__file__), "image_0.png")
    img = Image.open(image_path)
    img = img.resize((130, 130))
    photo = ImageTk.PhotoImage(img)
    img_label = tk.Label(root, image=photo, bg="#FDF6ED")
    img_label.image = photo
    img_label.pack(pady=(15, 5))
except:
    tk.Label(root, text="※ image_0.png が見つかりません", bg="#FDF6ED").pack(pady=10)

tk.Label(
    root,
    text="大学合格判定アプリ",
    font=("メイリオ", 22, "bold"),
    bg="#FDF6ED"
).pack(pady=10)

frame = tk.Frame(root, bg="#FDF6ED")
frame.pack(pady=10)

def add_row(row, label_text, widget):
    tk.Label(
        frame,
        text=label_text,
        font=("メイリオ", 11),
        bg="#FDF6ED",
        anchor="e",
        width=12
    ).grid(row=row, column=0, padx=8, pady=5)
    widget.grid(row=row, column=1, padx=8, pady=5)

grade_box = ttk.Combobox(frame, values=["1年生", "2年生", "3年生"], width=22)
grade_box.set("3年生")
add_row(0, "学年：", grade_box)

entry_school = tk.Entry(frame, width=25)
add_row(1, "高校名：", entry_school)

entry_hs = tk.Entry(frame, width=25)
add_row(2, "高校偏差値：", entry_hs)

entry_univ = tk.Entry(frame, width=25)
add_row(3, "志望大学名：", entry_univ)

entry_dept = tk.Entry(frame, width=25)
add_row(4, "志望学部名：", entry_dept)

entry_us = tk.Entry(frame, width=25)
add_row(5, "大学偏差値：", entry_us)

entry_rank = tk.Entry(frame, width=25)
add_row(6, "学年順位：", entry_rank)

entry_total = tk.Entry(frame, width=25)
add_row(7, "学年人数：", entry_total)

btn = tk.Button(
    root,
    text="判定！",
    command=judge,
    bg="#2FBF4A",
    fg="white",
    font=("メイリオ", 16, "bold"),
    width=10
)
btn.pack(pady=20)

root.mainloop()